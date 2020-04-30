import tkinter as tk
from tkinter import filedialog, Text
import os
import numpy as np
import cv2

class Buttons:
    def __init__ (self):
        self.dir = dir

    def criar_pasta(self): # Criando pasta de cadastro
        if not os.path.exists('cadastro'): # Confere se a pasta já existe
            os.mkdir('cadastro')
            print('A pasta foi criada com sucesso!')
        self.dir = 'cadastro'

    def openImage(self):
        filename = filedialog.askopenfilename(initialdir='/home/nodyer/Área de Trabalho', title="Select File", filetypes=(("Images","*png"),("all files","*.*")))
        print(filename)

    def openWebcam(self, entry): # Tirar foto para o cadastro
        nome_foto = entry + '.png'
        self.dir += '/' + nome_foto

        cap = cv2.VideoCapture(0)

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

    def openWindow(self):
        root2 = tk.Tk()
        root.destroy()
        root2.mainloop()

    def fecha(self, entry, root):
        print('Seu nome é', entry)
        root.destroy()



# root = tk.Tk()

# canvas = tk.Canvas(root, height=350, width=400, bg='#263D42')
# canvas.pack()

# frame = tk.Frame(root, bg='white')
# frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.1)

# L1 = tk.Label(root, text="User Name")
# L1.pack()
# E1 = tk.Entry(root, bd =5)
# E1.pack()
#---------------------------------------------------------------------------------------------------------
# openImage = tk.Button(root, text='Image', padx=10, pady=5, fg='white', bg='#263D42', command=openImage)
# openImage.pack()

# openWebcam = tk.Button(root, text='Webcam', padx=10, pady=5, fg='white', bg='#263D42', command=openCam)
# openWebcam.pack()

# openWindow = tk.Button(root, text='Window', padx=10, pady=5, fg='white', bg='#263D42', command=openWindow)
# openWindow.pack()

# sendText = tk.Button(root, text='Send', padx=10, pady=5, fg='white', bg='#263D42', command=lambda: texto(E1.get()))
# openWindow.pack()
#---------------------------------------------------------------------------------------------------------

# entry = tk.Entry(frame, font=40)
# entry.place(relwidth=0.65, relheight=1)

# button = tk.Button(frame)
# button.place(relx=0.7, relheight=1, relwidth=0.3)

# lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
# lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# label = tk.Label(lower_frame)
# label.place(relwidth=1, relheight=1)

# root.mainloop()


# ------------------------------------------------------- #
# Sequência: (sem edição)
# 1. Nome
# a) cadastrada? (PASS)
# b) não cadastrada? (OPEN WINDOW)
#
# 2. Cadastro
# a) dois botões: 
#   1 - webcam (ABRE)
#   2 - foto (ENVIA)
# ------------------------------------------------------- #