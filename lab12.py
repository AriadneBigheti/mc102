lista = int(input()).split()

largura=len(lista)

def maior_numero(1,lista):
    anterior=lista[0]
    maior=anterior
    menor=anterior
    if len(lista)!=1:
        for i in range (1, len(lista)):
        if i>anterior:
            maior=i
        else:
            menor=i
        anterior= i

return maior
