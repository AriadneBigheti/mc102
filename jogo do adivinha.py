ini = int(input())
fim = int(input())

print("Pense em um número de", ini, "à", fim)

meio=(ini+fim)//2

while ini!=meio:
    print("Seu número é menor ou igual à", meio,"? (S/N)")
    r = input()
    if r=="S":
        fim = meio
        meio = (ini+fim)//2
    else:
        ini = meio +1
        meio = (ini+fim)//2

print("Seu número é igual à", ini, "? (S/N)")
r = input()

if r =="S":
    print("Adivinhei seu número")
else:
    print("Seu número é", fim)


        
    
