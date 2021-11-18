valor = int(input("Digite um valor: "))

v = valor
anterior = 10
adjacente = False

if 0<=valor<10:
    print("O valor digitado não possui algarismos adjacentes iguais.")
else:
    while v!=0:
        r= v%10
        if anterior == r:
            print("O valor digitado possui dois algarismos adjacentes iguais a", r)
            adjacente = True
        else:
            anterior = r
        v = v//10
    if not adjacente:
        print("O valor digitado não possui algarismos adjacentes iguais.")
