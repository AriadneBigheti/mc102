valor = int(input("Digite um valor inteiro maior que zero: "))

soma = 0
v = valor

if 0<= valor< 10:
    print(" A soma dos algarismos é:", valor)
else:             
    while v>9 :
        resto = v%10
        soma = soma + resto
        v = v//10
    soma = soma + v        
    print("A soma dos algarismos é:", soma)
