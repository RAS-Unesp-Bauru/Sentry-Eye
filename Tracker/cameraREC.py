import face_recognition
import cv2
from multiprocessing import Process, Manager, cpu_count, set_start_method
import time
import numpy
import threading
import platform

import testetrack 
import SLR
from cadastro import Cadastro



# This is a little bit complicated (but fast) example of running face recognition on live video from your webcam.
# This example is using multiprocess.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

#-----------------------------------------------------------------------------------------------------------
# Get next worker's id
def next_id(current_id, worker_num):
    if current_id == worker_num:
        return 1
    else:
        return current_id + 1


# Get previous worker's id
def prev_id(current_id, worker_num):
    if current_id == 1:
        return worker_num
    else:
        return current_id - 1


# A subprocess use to capture frames.
def capture(read_frame_list, Global, worker_num):
    # Get a reference to webcam #0 (the default one)
    video_capture = cv2.VideoCapture(0)
    # video_capture.set(3, 640)  # Width of the frames in the video stream.
    # video_capture.set(4, 480)  # Height of the frames in the video stream.
    # video_capture.set(5, 30) # Frame rate.
    #print("Width: %d, Height: %d, FPS: %d" % (video_capture.get(3), video_capture.get(4), video_capture.get(5)))

    while not Global.is_exit:
        # If it's time to read a frame
        if Global.buff_num != next_id(Global.read_num, worker_num):
            # Grab a single frame of video
            ret, frame = video_capture.read()
            read_frame_list[Global.buff_num] = frame
            Global.buff_num = next_id(Global.buff_num, worker_num)
        else:
            time.sleep(0.01)

    # Release webcam
    video_capture.release()


# Many subprocess use to process frames.
def process(worker_id, read_frame_list, write_frame_list, Global, worker_num):
    
    known_face_encodings = Global.known_face_encodings
    known_face_names = Global.known_face_names
    
    #cache = []
    cache = None

    obj_teste = testetrack.Object_Tracking()
    obj_teste.start()    
    
    while not Global.is_exit:

        # Wait to read
        while Global.read_num != worker_id or Global.read_num != prev_id(Global.buff_num, worker_num):
            # If the user has requested to end the app, then stop waiting for webcam frames
            if Global.is_exit:
                break

            time.sleep(0.01)

        # Delay to make the video look smoother
        time.sleep(Global.frame_delay)

        # Read a single frame from frame list
        frame_process = read_frame_list[worker_id]

        # Expect next worker to read frame
        Global.read_num = next_id(Global.read_num, worker_num)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame = frame_process[:, :, ::-1]

        #Find all the faces and face encodings in the frame of video, cost most time
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
            
        #Criação dos retângulos
        ret0 = SLR.criaRet(SLR.altura_ret_0, SLR.largura_ret_0, SLR.roxo, frame_process, 1) #Cria R0
        lista_ret = SLR.criaListaRetangulos(ret0, 3, frame_process) #Cria lista de retângulos após R0 
    
        # Loop through each face in this frame of video

        #print("Status do track: %d" %(object_tracking.getStatus()))

        if face_encodings==[]:
            
            #Wait to write
            #print(cache)
            if cache!=None:
                #coordenadas = (cache[0], cache[1], cache[2], cache[3])
                coordenadas = cache
                #coordenadas = (181, 72, 367, 253)
                obj_teste.setFrame(frame_process)
                obj_teste.setCoord(coordenadas) 
                obj_teste.start_tracking()
                #print("Status do obj na classe principal: %d" % (obj_teste.getStatus()))

                p1 = obj_teste.getP1()
                p2 = obj_teste.getP2()
                #print(p1)
                #print(p2)
                #print(coordenadas)
                if(p1!=None and p2!=None):
                    cv2.rectangle(frame_process, (p1[0], p1[1]), (p2[0], p2[1]), (15, 130, 0), 2)
                    SLR.conditions([p1[1], p2[0], p2[1], p1[0]], lista_ret)

        else:
            for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

                name = "Desconhecido"

                # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                    #print(face_locations[0])
                    SLR.conditions(face_locations[0], lista_ret)
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                    #cache = [left*1.1, top*1.1, right*0.5, bottom*0.5]
                    #cache = (left*1.1, top*1.1, right*0.5, bottom*0.5)
                    cache = (right*0.8, bottom*0.5, left*0.35, top*0.8)
                    #cache = [left, top, right, bottom]
                    #print(type(cache[0]))
                    coordenadas = None
                    obj_teste.stop_tracking()
                    
                
                # Draw a box around the face
                
                cv2.rectangle(frame_process, (left, top), (right, bottom), (0, 0, 255), 2)
                
                

                # Draw a label with a name below the face
                cv2.rectangle(frame_process, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame_process, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        
             

        while Global.write_num != worker_id:
            time.sleep(0.01)

        # Send frame to global
        write_frame_list[worker_id] = frame_process

        # Expect next worker to write frame
        Global.write_num = next_id(Global.write_num, worker_num)


if __name__ == '__main__':

    pessoa1 = Cadastro()
    pessoa1.criar_pasta()
    pessoa1.tirar_foto(0) # webcam = 0 / video = 1

    coordenadas_obj_tracking = ()

    # Global variables
    Global = Manager().Namespace()
    Global.buff_num = 1
    Global.read_num = 1
    Global.write_num = 1
    Global.frame_delay = 0
    Global.is_exit = False
    read_frame_list = Manager().dict()
    write_frame_list = Manager().dict()

    # Number of workers (subprocess use to process frames)
    if cpu_count() > 2:
        worker_num = cpu_count() - 1  # 1 for capturing frames
    else:
        worker_num = 2

    # Subprocess list
    p = []

    # Create a thread to capture frames (if uses subprocess, it will crash on Mac)
    p.append(threading.Thread(target=capture, args=(read_frame_list, Global, worker_num,)))
    p[0].start()
    

    # Load a sample picture and learn how to recognize it.
    target_image = face_recognition.load_image_file(pessoa1.dir)
    target_face_encoding = face_recognition.face_encodings(target_image)[0]

    # Create arrays of known face encodings and their names
    Global.known_face_encodings = [
        target_face_encoding
    ]

    Global.known_face_names = [
        pessoa1.nome
    ]

    # Create workers
    for worker_id in range(1, worker_num + 1):
        p.append(Process(target=process, args=(worker_id, read_frame_list, write_frame_list, Global, worker_num,)))
        p[worker_id].start()
   
    # Start to show video
    last_num = 1
    fps_list = []
    tmp_time = time.time()

    while not Global.is_exit:
        while Global.write_num != last_num:
            last_num = int(Global.write_num)

            # Calculate fps
            delay = time.time() - tmp_time
            tmp_time = time.time()
            fps_list.append(delay)
            if len(fps_list) > 5 * worker_num:
                fps_list.pop(0)
            fps = len(fps_list) / numpy.sum(fps_list)
            print("fps: %.2f" % fps)

            # Calculate frame delay, in order to make the video look smoother.
            # When fps is higher, should use a smaller ratio, or fps will be limited in a lower value.
            # Larger ratio can make the video look smoother, but fps will hard to become higher.
            # Smaller ratio can make fps higher, but the video looks not too smoother.
            # The ratios below are tested many times.
            if fps < 6:
                Global.frame_delay = (1 / fps) * 0.75
            elif fps < 20:
                Global.frame_delay = (1 / fps) * 0.5
            elif fps < 30:
                Global.frame_delay = (1 / fps) * 0.25
            else:
                Global.frame_delay = 0

            # Display the resulting image
            cv2.imshow('Video', write_frame_list[prev_id(Global.write_num, worker_num)])

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            object_tracking.stop_tracking()
            Global.is_exit = True
            break

        time.sleep(0.01)

    video_capture.release()
    # Quit
    cv2.destroyAllWindows()
