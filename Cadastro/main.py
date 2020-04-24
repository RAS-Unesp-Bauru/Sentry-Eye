from cadastro import Cadastro

p1 = Cadastro()
p1.criar_pasta()
p1.tirar_foto(0) # webcam = 0 / video = 1

print(p1.dir)
