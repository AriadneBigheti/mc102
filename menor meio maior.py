a = int(input())
b = int(input())
c = int(input())

if a>=b and a>=c:
    maior=a
    if b>c:
        menor=c
        meio=b
    else:
        menor=b
        meio=c
        
elif b>=a and b>=c:
    maior=b
    if a>c:
        menor=c
        meio=a
    else:
        menor=a
        meio=c
elif c>=a and c>=b:
    maior=c
    if a>b:
        menor=b
        meio=a
    else:
        menor=a
        meio=b

print(menor, meio, maior)

    
