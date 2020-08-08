from os import system
import face_recognition
import cv2
import numpy as np
import objTracking
import RBS
import threading
import serial
from imutils.video import FPS
from sentryFont import Sentry
from registration import Registration
from setSpeed import SetSpeed
import arduino

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
jump_booster = 0
jump = 0
string_arduino = ""

option1 = SetSpeed()
speed = option1.get_speed()

if speed == 's':
    jump_booster = 1

if speed == 'm':
    jump_booster = 2

if speed == 'f':
    jump_booster = 3

print("You chose the {} velocity".format(speed))

arduino_connection = arduino.createConnection('/dev/ttyUSB0') # Change it for your port here.
arduino.setServoInCenter(arduino_connection)

person1 = Registration()
person1.create_file()
person1.take_photo(0) # webcam = 0 / video = 1

video_capture = cv2.VideoCapture(0)

fps = FPS()
fps.start()


# Load a sample picture and learn how to recognize it.
target_image = face_recognition.load_image_file(person1.dir)
target_face_encoding = face_recognition.face_encodings(target_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    target_face_encoding
]

known_face_names = [
    person1.name
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
cache = None 

sentry = Sentry(20, arduino_connection) #The first argumment here is the sentry jump

tracker = cv2.TrackerKCF_create()
tracker_flag = 0

while True:
    # Grab a single frame of video
    print("\n")
    ret, frame = video_capture.read()

    fps.update()
    fps.stop()

    sentry.setFrame(frame)
    
    cv2.putText(frame, "FPS: {:.2f}".format(fps.fps()), (31, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

    #cv2.putText(frame, fps.fps(), (frame.shape[0]*0.12, frame.shape[1]*0.8), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 129, 35), 2)
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    
    # Only process every other frame of video to save time

    if process_this_frame:

        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        rect0 = RBS.createRet(RBS.rect_height_0, RBS.rect_width_0, RBS.purple, frame, 1) #Create R0
        rect_list = RBS.createsRectangleList(rect0, 3, frame) #Create list of rectangles after R0 

        face_names = []

        if(face_encodings==[]):
            #print("No target was recognized")

            
            if(cache!=None):
                #print("Target lost")
                
                coordinates = (cache[0], cache[1], cache[2], cache[3])

                if tracker_flag==1:
                    tracker = cv2.TrackerKCF_create()
                    tracker_flag = 0

                if coordinates is not None:
                    tracker.init(frame, coordinates)
                
                    (success, box) = tracker.update(frame)

                    if success:

                        sentry.stop_sentry_mode()

                        (left_tracker, top_tracker, w, h) = [int (v) for v in box]
                        
                        right_tracker = left_tracker + h
                        bottom_tracker = top_tracker + h
                        p1 = (left_tracker, top_tracker)
                        p2 = (right_tracker, bottom_tracker)

                        cv2.rectangle(frame, p1, p2, (0,0,0), 2)

                        #Send
                        rectAndDirect = RBS.conditions([top_tracker, right_tracker, bottom_tracker, left_tracker], rect_list)

                        if rectAndDirect is not None:
                            rectangle_1 = rectAndDirect[0][0]
                            direction_1 = rectAndDirect[0][1]
                            rectangle_2 = '-'
                            direction_2 = 0

                            if len(rectAndDirect)==2:
                                rectangle_2 = rectAndDirect[1][0]
                                direction_2 = rectAndDirect[1][1] 
                            
                            system("clear")

                            if rectangle_1 == 'l' or rectangle_1 == 'r':
                                print("Velocidade Horizontal: ", rectangle_1, end='\n')
                                print("Velocidade Vertical: ", rectangle_2, end='\n')

                            if rectangle_1 == 't' or rectangle_1 == 'b':
                                print("Velocidade Horizontal: ", rectangle_2, end='\n')
                                print("Velocidade Vertical: ", rectangle_1, end='\n')
                            
                            arduino.sendArduino(arduino_connection, direction_1, rectangle_1, direction_2, rectangle_2, jump_booster) 
                    
                    elif not success:
                        if(sentry.getStatus()==0):
                            sentry.startTimer()

        
        else:
            #print("Possible target acquired")

            sentry.stop_sentry_mode()

            for face_encoding in face_encodings:

                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

                name = "Unknown"

                # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                # first_match_index = matches.index(True)
                # name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)

                if matches[best_match_index]:
                    #print("Target found.")

                    name = known_face_names[best_match_index]

                    top = face_locations[0][0]
                    right = face_locations[0][1]
                    bottom = face_locations[0][2]
                    left = face_locations[0][3]

                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4

                    #Send
                    rectAndDirect = RBS.conditions([top, right, bottom, left], rect_list) 

                    if rectAndDirect is not None:
                        rectangle_1 = rectAndDirect[0][0]
                        direction_1 = rectAndDirect[0][1]
                        rectangle_2 = '-'
                        direction_2 = 0

                        if len(rectAndDirect)==2:
                            rectangle_2 = rectAndDirect[1][0]
                            direction_2 = rectAndDirect[1][1] 
                        
                        system("clear")

                        if rectangle_1 == 'l' or rectangle_1 == 'r':
                            print("Velocidade Horizontal: ", rectangle_1, end='\n')
                            print("Velocidade Vertical: ", rectangle_2, end='\n')

                        if rectangle_1 == 't' or rectangle_1 == 'b':
                            print("Velocidade Horizontal: ", rectangle_2, end='\n')
                            print("Velocidade Vertical: ", rectangle_1, end='\n')
                        
                        arduino.sendArduino(arduino_connection, direction_1, rectangle_1, direction_2, rectangle_2, jump_booster)

                    cache = None
                    cache = [left, top, right*0.5, bottom*0.5]
                    coordinates = None
                    tracker_flag = 1

                face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# Release handle to the webcam
arduino.closeConnection(arduino_connection)
sentry.stop_sentry_mode()
video_capture.release()
cv2.destroyAllWindows()

