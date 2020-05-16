for i in range(len(lista_ret[1]):
    teste_esquerda = lista_ret[n][0][0] - left
    
    if teste_esquerda > 0:
        print( "passou à esquerda do retângulo {}".format(n) )
        break

for i in range(len(lista_ret[1]):
    teste_direita = lista_ret[n][1][0] - right
    
    if teste_direita < 0:
        print( "passou à direita do retângulo {}".format(n) )
        break

for i in range(len(lista_ret[1]):
        teste_cima = lista_ret[n][0][1] - top
        
    if teste_cima < 0:
        print( "passou acima do retângulo {}".format(n) )
        break

for i in range(len(lista_ret[1]):
    teste_baixo = lista_ret[n][1][1] - bottom
    
    if teste_baixo > 0:
        print( "passou abaixo do retângulo {}".format(n) )
        break