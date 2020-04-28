import face_recognition
import cv2
from multiprocessing import Process, Manager, cpu_count, set_start_method
import time
import numpy
import threading
import platform
#--------------------------------------------------------
import os


# This is a little bit complicated (but fast) example of running face recognition on live video from your webcam.
# This example is using multiprocess.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

class FaceRecognition:
    def __init__(self, photo):
        self.photo = photo
        name = self.photo.replace('Cadastro/', '').replace('.png', '')
        self.name = name

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
            
            dimensions = frame_process.shape
            #-----------------------------------------------------------------------------------------------------------
            def criaRetangulos(numero_de_retangulos):
                height = dimensions[0] / 2
                width = dimensions[1] / 2

                #Divide a quantidade que será iterada a altura e largura. Também inicia a menor velocidade.
                altura_por_retangulo = height / numero_de_retangulos
                largura_por_retangulo = width / numero_de_retangulos
                menor_velocidade = 1

                #Inicia uma lista vazia
                lista_retangulos = []
                lista_retangulos_pontos = []

                iteracao = 0
                #Loop para formar a lista
                for i in range(numero_de_retangulos+1):

                    #Altura e largura da respectiva iteração. A cada Loop muda a posição
                    altura_retangulo = height - (altura_por_retangulo * numero_de_retangulos)
                    largura_retangulo = width - (largura_por_retangulo * numero_de_retangulos)

                    #Aumenta a velocidade, deve ser futuramente testada em relação ao último retângulo para conferir aonde o target
                    #está realmente contido
                    velocidade = menor_velocidade*iteracao

                    #Adiciona as propriedades dessa iteração a lista
                    novo_retangulo = [largura_retangulo, altura_retangulo, velocidade]
                    lista_retangulos.append(novo_retangulo)

                    numero_de_retangulos -= 1
                    iteracao += 1
                    
                    cor_laranja = (0, 165, 255) #BGR

                    for i in range(1, len(lista_retangulos)):
                        esquerda = int(width) - int(lista_retangulos[i][0]) #x0
                        direita = int(width) + int(lista_retangulos[i][0]) #x1

                        cima = int(height) - int(lista_retangulos[i][0]) #y0
                        baixo = int(height) + int(lista_retangulos[i][0]) #y1

                        #Pontos principais para formarem o retângulo
                        ponto01 = (esquerda, cima) #(x0, y0)
                        ponto02 = (direita, baixo) #(x1, y1)

                        #Salva a imagem desenhada como 'nova_img'
                        nova_img = cv2.rectangle(frame_process, ponto01, ponto02, cor_laranja, 1)

                        ponto01_lista = [esquerda, cima] #(x0, y0)
                        ponto02_lista = [direita, baixo] #(x1, y1)

                        retangulo = [ponto01_lista, ponto02_lista, vel]

                        lista_retangulos_pontos.append(pontos)

                return lista_retangulos_pontos


            #-----------------------------------------------------------------------------------------------------------
            #Limita coordenadas#---------------------------------------------------------------------------
            '''cor_laranja = (0, 165, 255) #BGR

            altura = 300
            largura = 200

            esquerda = int(dimensions[1]/2) - int(largura/2) #x0
            direita = int(dimensions[1]/2) + int(largura/2) #x1

            cima = int(dimensions[0]/2) - int(altura/2) #y0
            baixo = int(dimensions[0]/2) + int(altura/2) #y1

            #pontos principais para formarem o retângulo
            ponto01 = (esquerda, cima) #(x0, y0)
            ponto02 = (direita, baixo) #(x1, y1)

            cv2.rectangle(frame_process, ponto01, ponto02, cor_laranja, 1)
            '''#-----------------------------------------------------------------------------------------------
                
            #numero_de_retangulos = int(input("digite aqui o número de retângulos: "))
            lista_ret = criaRetangulos(4)
            # Loop through each face in this frame of video

            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

                name = "Desconhecido"

                # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                    if top < lista_ret[0][0][1]:
                        print('Passou cima')
                    if bottom > lista_ret[0][1][1]:
                        print('Passou baixo')
                    if right > lista_ret[0][1][0]:
                        print('Passou lado direito')
                    if left < lista_ret[0][0][0]:
                        print('Passou esquerda')
                    
                    #armazena coordenadas target----------
                    #cache = [[left, top], [right, bottom]]
                    #-------------------------------------

                # Draw a box around the face
                cv2.rectangle(frame_process, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(frame_process, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame_process, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # Wait to write
            while Global.write_num != worker_id:
                time.sleep(0.01)

            # Send frame to global
            write_frame_list[worker_id] = frame_process

            # Expect next worker to write frame
            Global.write_num = next_id(Global.write_num, worker_num)


    def FaceRecognition():

        # Fix Bug on MacOS
        if platform.system() == 'Darwin':
            set_start_method('forkserver')

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
        target_image = face_recognition.load_image_file(self.photo)
        target_face_encoding = face_recognition.face_encodings(target_image)[0]

        """target_image_02 = face_recognition.load_image_file("target_02.png")
        target_face_encoding = face_recognition.face_encodings(target_image_02)[1]

        target_image_03 = face_recognition.load_image_file("target_03.png")
        target_face_encoding = face_recognition.face_encodings(target_image_03)[2]

        target_image_04 = face_recognition.load_image_file("target_04.png")
        target_face_encoding = face_recognition.face_encodings(target_image_04)[3]
    """
        # Load a second sample picture and learn how to recognize it.
        #biden_image = face_recognition.load_image_file("biden.jpg")
        #biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

        # Create arrays of known face encodings and their names
        Global.known_face_encodings = [
            target_face_encoding
        #    biden_face_encoding
        ]
        Global.known_face_names = [
            self.name
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
                Global.is_exit = True
                break

            time.sleep(0.01)

        # Quit
        cv2.destroyAllWindows()
