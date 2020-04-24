import os
import cv2

class Cadastro:
    def __init__ (self):
        self.dir = dir
        self.nome = input('Digite seu nome para o cadastro: ')

    def criar_pasta(self): # Criando pasta de cadastro
        if not os.path.exists('cadastro'): # Confere se a pasta já existe
            os.mkdir('cadastro')
            print("A pasta foi criada com sucesso!")
        self.dir = 'cadastro'

    def tirar_foto(self, video_ou_webcam): # Tirar foto para o cadastro
        nome_foto = self.nome + '.png'
        self.dir += '/' + nome_foto

        if os.path.exists(self.dir): # Se a pessoa já for cadastrada, não fará novamente. 
            print('Você já está cadastrado.')

        else:
            print('Você não está cadastrado, faça agora!')

            if video_ou_webcam == 0:
                cap = cv2.VideoCapture(0)
            
            elif video_ou_webcam == 1:
                nome_video = input('Nome do arquivo de vídeo: ')
                cap = cv2.VideoCapture(nome_video)
            
            while True:
                try:
                    check, frame = cap.read()
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