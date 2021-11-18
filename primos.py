num = int(input())
lista_divisores= []

for i in range(1, num+1):
    if num%i == 0 :
        lista_divisores.append(i)

if len(lista_divisores)==2:
    if 1 in lista_divisores and num in lista_divisores:
        print("É primo")
else:
    print("Não é primo, seus divisores são: ", lista_divisores)
