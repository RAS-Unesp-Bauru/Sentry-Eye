import face_recognition
import cv2
import numpy as np
import testetrack 
import SLR
from cadastro import Cadastro
import threading

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
url = "http://192.168.42.129:8080/video"

pessoa1 = Cadastro()
pessoa1.criar_pasta()
pessoa1.tirar_foto(0) # webcam = 0 / video = 1

video_capture = cv2.VideoCapture(0)


# Load a sample picture and learn how to recognize it.
target_image = face_recognition.load_image_file(pessoa1.dir)
target_face_encoding = face_recognition.face_encodings(target_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    target_face_encoding
]

known_face_names = [
    pessoa1.nome
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

cache = []

obj_teste = testetrack.Object_Tracking()
obj_teste.start()    

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    
    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        ret0 = SLR.criaRet(SLR.altura_ret_0, SLR.largura_ret_0, SLR.roxo, frame, 1) #Cria R0
        lista_ret = SLR.criaListaRetangulos(ret0, 3, frame) #Cria lista de retângulos após R0 

        face_names = []
        #print(face_encodings)

        if(face_encodings==[]):
            #print("Tem ninguem nao truta")url
            
            if(cache!=[]):
                #print("Ja teve alguem mas sumiu")
                coordenadas = (cache[0], cache[1], cache[2], cache[3])
               
                obj_teste.setFrame(frame)
                obj_teste.setCoord(coordenadas) 
                obj_teste.start_tracking()

                p1 = obj_teste.getP1()
                p2 = obj_teste.getP2()
                
                if(p1!=None and p2!=None):
                    cv2.rectangle(frame, (p1[0], p1[1]), (p2[0], p2[1]), (15, 130, 0), 2)
                    SLR.conditions([p1[1], p2[0], p2[1], p1[0]], lista_ret)
        
        else:
            #print("Achei alguem aqui")

            for face_encoding in face_encodings:

                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

                name = "Desconhecido"

                # # If a match was found in known_face_encodings, just use the first one.
                #if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)

                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    
                    top = face_locations[0][0]
                    right = face_locations[0][1]
                    bottom = face_locations[0][2]
                    left = face_locations[0][3]

                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4
                    SLR.conditions([top, right, bottom, left], lista_ret)
                    
                    cache = []
                    cache = [left, top, right*0.5, bottom*0.5]

                    coordenadas = None
                    obj_teste.stop_tracking()
            

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
        obj_teste.stop_tracking()
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
