import os
import cv2

class Cadastro:
    def __init__ (self):
        self.dir = dir
        self.nome = input('Digite seu nome para o cadastro: ')

    def criar_pasta(self):
        if not os.path.exists('cadastro'):
            os.mkdir('cadastro')
            print("A pasta foi criada com sucesso!")
        self.dir = 'cadastro'

    def tirar_foto(self, video_ou_webcam):
        key = cv2. waitKey(1)
        nome_foto = self.nome + '.png'
        self.dir += '/' + nome_foto

        if video_ou_webcam == 0:
            cap = cv2.VideoCapture(0)
        
        elif video_ou_webcam == 1:
            nome_video = input('Nome do arquivo de vídeo: ')
            cap = cv2.VideoCapture(nome_video)
        
        while True:
            try:
                check, frame = cap.read()
                '''
                print(check) #prints true as long as the webcam is running
                print(frame) #prints matrix values of each framecd 
                '''
                cv2.imshow("Capturando", frame)
                key = cv2.waitKey(1)
                if key == ord('s'): 
                    cv2.imwrite(filename=self.dir, img=frame)
                    cap.release()
                    print("Foto salva!")
                    break
                
                elif key == ord('q'):
                    cap.release()
                    cv2.destroyAllWindows()
                    break
            
            except(KeyboardInterrupt):
                print("Desligando a câmera.")
                webcam.release()
                print("Câmera desligada.")
                print("Programa encerrado.")
                cv2.destroyAllWindows()
                break