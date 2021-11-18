tam_sequencia= int(input("Digite o tamanho da sequencia:" ))
anterior = int(input("Digite o primeiro numero:" ))
maior=anterior
menor=anterior

if tam_sequencia !=1:   
    for i in range (1, tam_sequencia):
        i = int(input("Digite o próximo numero:"))
        if i>anterior:
            maior=i
        else:
            menor=i
        anterior= i

print("O menor numero é:", menor)
print("O maior numero é:", maior)

