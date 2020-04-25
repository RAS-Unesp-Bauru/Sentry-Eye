import cv2

#from google.colab.patches import cv2_imshow


###Código atualmente pega apenas UM ponto, assim demonstrando apenas o esqueleto
###da ideia. O ideal seria achar o centro da imagem e a partir dai refletir nos
###2 quadrantes opostos para formar o retângulo com centro no meio.

video = cv2.VideoCapture(0)
ret, cap = video.read()

#Lê a imagem em binário para garantir que as shape 0 e shape 1 sejam height e width
#cap = cv2.imread(r'/content/alex-lacamoire.png', 0)

dimensions = cap.shape

#Confere quantos pixeis de altura e largura o objeto possui
height = dimensions[0] / 2
width = dimensions[1] / 2

print("\n altura x:     ", width, "\n largura y:    ", height,"\n")

#Pede ao usuário um número arbitrário de retângulos
numero_de_retangulos = int(input("digite aqui o número de retângulos: "))

#Divide a quantidade que será iterada a altura e largura. Também inicia a menor velocidade.
altura_por_retangulo = height / numero_de_retangulos
largura_por_retangulo = width / numero_de_retangulos
menor_velocidade = 1

#Inicia uma lista vazia
lista_retangulos = []


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

#Printa a lista formada, cada index é as propriedades daquele retângulo e deve ser acessado como lista_retangulos[n]
#print(lista_retangulos, '\n')


#Define cores para os retângulos e aloca 'nova_img' na memória
cor_laranja = (0, 165, 255) #BGR
nova_img = cap

while(True):
    ret, cap = cap.read()

    ###Seguindo o esquema de criação de retângulos anterior, agora desenha os retângulos
    ###a partir do centro da imagem.

    #Define o Loop de criação de retângulos. O index 1 atualmente é 0,0,0, então estou
    #passando direto por ele
    for i in range(1, len(lista_retangulos)):
        esquerda = int(width) - int(lista_retangulos[i][0]) #x0
        direita = int(width) + int(lista_retangulos[i][0]) #x1

        cima = int(height) - int(lista_retangulos[i][0]) #y0
        baixo = int(height) + int(lista_retangulos[i][0]) #y1

        #Pontos principais para formarem o retângulo
        ponto01 = (esquerda, cima) #(x0, y0)
        ponto02 = (direita, baixo) #(x1, y1)

        #Salva a imagem desenhada como 'nova_img'
        nova_img = cv2.rectangle(cap, ponto01, ponto02, cor_laranja, 1)

    #Mostra a imagem após a construção de todos retângulos
    cv2.imshow('imagenzinha', nova_img)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        print("Forcefully Closed")
        cv2.destroyAllWindows()