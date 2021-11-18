elem = input().zfill(3)
lista = input().split()
espaco = " "
print("Elemento procurado:", elem)

for i in range(len(lista)):
    lista[i] = lista[i].zfill(3)

def imprime_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])-1):
            c = len(matriz[i])-1
            print(matriz[i][j], end='')
        print(matriz[i][c])
    return

def moldura(lista):
    matriz=[]
    linha1= []
    linha1.append("+")
    for i in range(len(lista)):
        linha1.append(5*"-")
        linha1.append("+")
    matriz.append(linha1)
    linha2 = []
    linha2.append("|")
    for i in range(len(lista)):
        linha2.append(espaco+lista[i]+espaco)
        linha2.append("|")  
    matriz.append(linha2)
    matriz.append(linha1)

    return matriz

matriz = moldura(lista)
imprime_matriz(matriz)

def meio_moldura(matriz, meio, lista):
    matriz_ = [s.copy() for s in matriz]
    matriz_[0][2*meio+1] = 5*"="
    matriz_[1][2*meio+1] = "|"+lista[meio]+"|"
    matriz_[2][2*meio+1] = 5*"="
    return matriz_


def moldura_nova(matriz, lista, ini, fim):
    matriz_= [s.copy() for s in matriz]
    if ini!=0:
        for i in range(3):
            for j in range(0,ini*2):
                aux =len(matriz_[i][j])
                matriz_[i][j]= aux*" "
                
        if lista[fim]!= matriz[1][-2]:
            for i in range(3):
                for j in range((fim+1)*2+1,len(matriz[i])):
                    n = (fim+1)*2+1
                    del (matriz_[i][n])
    else:
        matriz_ = moldura(lista[ini:fim+1])    
    return matriz_        

for i in range(len(lista)-1):
    if lista[i]>lista[i+1]:
        print("Lista nao ordenada")
        ordenacao = False
        break
    else:
        ordenacao = True

if ordenacao:
    ini = 0
    fim = len(lista)-1
    meio = (ini+fim)//2
    aux = meio_moldura(matriz, meio, lista)
    imprime_matriz(aux)
    matriz_nova = [s.copy() for s in matriz]
    lista_nova = lista[:]

    while ini<=fim and len(lista_nova)>1:
        if elem==lista[meio]:
            print("Encontrado na posicao:", meio)
            break
        elif elem<lista[meio]:
            fim = meio-1
            meio = (ini+fim)//2
            lista_nova=lista[ini:fim+1]
            matriz_nova = moldura_nova(matriz_nova, lista, ini, fim)
            aux = meio_moldura(matriz_nova, meio, lista)
            imprime_matriz(aux)
        else:                       #elem>lista[meio]
            ini = meio+1
            meio = (ini+fim)//2
            lista_nova=lista[ini:fim+1]
            matriz_nova = moldura_nova(matriz_nova, lista, ini, fim)
            aux = meio_moldura(matriz_nova, meio, lista)
            imprime_matriz(aux)

    if len(lista_nova)==1:
        if elem==lista[meio]:
            print("Encontrado na posicao:", meio)
        else:
            print("O elemento nao foi encontrado")

        
    
    
        


