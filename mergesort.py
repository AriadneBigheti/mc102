def merge(lista_A, lista_B):
    lista_C=[]
    if len(lista_A)==0:
        return lista_B
    elif len(lista_B)==0:
        return lista_A
    else:
        if lista_A[0]<=lista_B[0]:
            lista_C.append(lista_A[0])
            return lista_C + merge(lista_A[1:], lista_B)
        else:
            lista_C.append(lista_B[0])
            return lista_C + merge(lista_A, lista_B[1:])

def mergesort (lista):
    if len(lista)<=1:
        return lista
    else:
        meio = len(lista)//2
        lA = mergesort(lista[0:meio])
        lB = mergesort(lista[meio:])
        lM = merge(lA,lB)
        return lM
                       
