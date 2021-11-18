lista = input().split() #forma uma lista com str

for i in range(len(lista)):
    lista[i] = int(lista[i]) #transforma os elementos da lista em int

def maior_numero(lista): #encontra o maior numero da lista
    anterior=lista[0]
    maior=anterior
    if len(lista)!=1:
        for i in range (len(lista)):
            if lista[i]>maior:
                maior=lista[i]
            anterior= lista[i]
    return maior

def lista_quadro(lista): #tranforma uma lista numérica em quadro
    largura=len(lista)+2
    quadro=[]
    linha_pontilhada=[]
    for i in range(largura):
        linha_pontilhada.append(".")
    quadro.append(linha_pontilhada)

    altura = maior_numero(lista)
    for x in range (0,altura): #linha do quadro que estamos lendo
        linha = []
        linha.append(".")
        for i in range(len(lista)):
            if lista[i]< (altura - x) :
                linha.append(" ")
            else:
                linha.append("|")
        linha.append(".")
        quadro.append(linha)

    quadro.append(linha_pontilhada)
    return quadro


def formata_matriz(matriz): #printa a matriz que correspode ao quadro de forma correta
    for i in range(len(matriz)):
        for j in range(len(matriz[i])-1):
            c = len(matriz[i])-1
            print(matriz[i][j], end='')
        print(matriz[i][c])
    return


quadro = lista_quadro(lista)
formata_matriz(quadro)


lista_2= lista[:]
for x in range(len(lista)):     
    for i in range(len(lista)-1): #ordena a lista numérica por meio de bubble sort
        if lista[i]>lista[i+1]:
            lista_2[i], lista_2[i+1] = lista[i+1], lista[i] 
            quadro_2=lista_quadro(lista_2) #transforma a nova lista em quadro
            formata_matriz(quadro_2) #printa o novo quadro
        lista=lista_2[:]                  
