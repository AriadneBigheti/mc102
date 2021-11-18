n = int(input())
passos = int(input())
asc = input()
altura = 2**n

tela = [[asc for j in range(altura)] for i in range(altura)]

def imprime_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])-1):
            c = len(matriz[i])-1
            print(matriz[i][j], end='')
        print(matriz[i][c])
    return

def print_tela_com_moldura(tela, altura):
    linha1 = [["+"] + ["-" for i in range(altura+2)] + ["+"]]
    linha2 = [["|"] + [" " for i in range(altura+2)] + ["|"]]
    matriz = linha1 +linha2

    for x in range(altura):
        tela[x].append(" ")
        tela[x].append("|")
        tela[x] = ["|"] + [" "] + tela[x]

    matriz = matriz + tela + linha2 + linha1
    imprime_matriz(matriz)
    return

def subdividir_tela(tela, y, x, altura):  #x e y são as coordenadas do canto superior esquerdo do quadrado
    for i in range(y, y+altura//2):       #percorre altura//2 linhas
        for j in range(x, x+altura//4):   #percorre altura//4 colunas
            tela[i][j] = " "
            tela[i][((3*altura)//4)+j] = " "
    return tela

def desenhos_recursivos (tela, y, x, altura, passos):
    if passos == 0:
        return tela
    else:
        tela = subdividir_tela(tela, y, x, altura)
        tela = desenhos_recursivos(tela, y, x + altura//4, altura//2, passos-1)
        tela = desenhos_recursivos(tela, y + altura//2, x, altura//2, passos-1)
        tela = desenhos_recursivos(tela, y + altura//2, x + altura//2, altura//2, passos-1)
    return tela

aux = desenhos_recursivos(tela, 0, 0, altura, passos)
print_tela_com_moldura(aux, altura)
