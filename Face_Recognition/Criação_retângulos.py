import cv2 as cv
​
#cores
verde = (0, 0, 0)
azul = (0, 0, 10)
violeta = (0, 0, 20)
ciano = (0, 0, 30)
preto = (0, 0, 40)
​
​
#constantes 
velocidade_maxima = 1
tela_largura = 1
tela_altura = 1
​
​
#velocidades
v1 = 0.2 * velocidade_maxima 
v2 = 0.4 * velocidade_maxima
v3 = 0.6 * velocidade_maxima
v4 = 0.8 * velocidade_maxima
v5 = 1.0 * velocidade_maxima
​
​
#dimensões
largura_1 = 0.2 * tela_largura
altura_1 = 0.2 * tela_altura
​
largura_2 = 0.4 * tela_largura
altura_2 = 0.4 * tela_altura
​
largura_3 = 0.6 * tela_largura
altura_3 = 0.6 * tela_altura
​
largura_4 = 0.8 * tela_largura
altura_4 = 0.8 * tela_altura
​
largura_5 = 1.0 * tela_largura
altura_5 = 1.0 * tela_altura
​
​
#retangulos - cv.rectangle(frame, p1, p2, cor, espessura)
a = 1
b = 1
c = 1
d = 1
e = 1
​
#lista
retangulos = [(a, v1), (b, v2), (c, v3), (d, v4), (e, v5)]