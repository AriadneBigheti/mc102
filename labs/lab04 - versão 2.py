x= float(input())
y= float(input())
z= float(input())

if x>=y and x>=z:
    A=x
    B=y
    C=z
elif y>=x and y>=z:
    A=y
    B=x
    C=z
else:
    A=z
    B=x
    C=y
    
if (A>=(B+C) or B>=(A+C) or C>=(A+B)) or A<=0 or B<=0 or C<=0:
    print("Valores invalidos na entrada")
else:
    if A==B==C:
        print("Triangulo equilatero")
    elif A==B or A==C or B==C:
        print("Triangulo isosceles")
    else:
        print("Triangulo escaleno")
        
    if (A**2)==(B**2 + C**2):
        print("Triangulo retangulo")
    elif (A**2)<(B**2 + C**2):
        print("Triangulo acutangulo")    
    else:
        print("Triangulo obtusangulo")      

