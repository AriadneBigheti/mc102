A= float(input())
B= float(input())
C= float(input())

if (A>=(B+C) or B>=(A+C) or C>=(A+B)) or A<=0 or B<=0 or C<=0:
    print("Valores invalidos na entrada")
else:
    if A==B==C:
        print("Triangulo equilatero")
    elif A==B or A==C or B==C:
        print("Triangulo isosceles")
    if A!=B and A!=C and B!=C:
        print("Triangulo escaleno")
        
    if ((A**2)==(B**2 + C**2) and A>=B and A>=C) or ((B**2)==(A**2 + C**2) and B>=A and B>=C) or ((C**2)==(B**2 + A**2) and C>=B and C>=A):
        print("Triangulo retangulo")
    if ((A**2)<(B**2 + C**2) and A>=B and A>=C) or ((B**2)<(A**2 + C**2) and B>=A and B>=C) or ((C**2)<(B**2 + A**2) and C>=B and C>=A):
        print("Triangulo acutangulo")    
    if ((A**2)>(B**2 + C**2) and A>=B and A>=C) or ((B**2)>(A**2 + C**2) and B>=A and B>=C) or ((C**2)>(B**2 + A**2) and C>=B and C>=A):
        print("Triangulo obtusangulo")        
