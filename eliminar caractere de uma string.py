frase = input("Digite uma frase: ")
asc = input("Digite o caractere que vc quer eliminar da frase: ")
nova_frase = ""

for i in range(len(frase)):
    if frase[i] != asc:
        nova_frase += frase[i]

print("A frase final é:", nova_frase)
        
