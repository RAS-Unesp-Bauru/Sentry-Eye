from cadastro import Cadastro
from facerec_test import FaceRecognition as fr

p1 = Cadastro()
p1.criar_pasta()
p1.tirar_foto(0) # webcam = 0 / video = 1

print(p1.dir)

fr.faceREC(p1.dir)