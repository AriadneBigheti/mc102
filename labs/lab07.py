tipo = input()
asc = input()
dim = int(input())

if tipo != "Q" and tipo !="T" and tipo !="L" and tipo != "H" and tipo!= "O":
    print("Identificador invalido.")
    
elif dim<3:
    print("Dimensao invalida.")
    
else:
    if tipo == "Q":
        lado = dim
        for t in range(lado):
            for i in range(lado):
                print(asc, end='')
            print()
                          
            
    elif tipo == "T" or tipo =="L":
        altura = dim
        e = altura - 1
        for i in range(1, altura*2, 2):
            print(e*" ", i*asc, sep='')
            e = e -1            
     
        if tipo == "L":
            e = 1
            for i in  range(altura*2 -3, 0, -2): 
                print(e*" ", i*asc, sep='')
                e = e + 1
                            
    elif tipo =="H" or tipo== "O":
        lado = dim
        e = lado -1
        for i in range(lado, 3*lado - 1, 2):
            print(e*" ", i*asc, sep='')
            e = e - 1
            
        if tipo == "O":
            for i in range(0, lado-1, 1):
                print((3*lado-2)*asc)
                
        e = 1
        for i in range(3*lado - 4,lado-1, -2):
            print(e*" ", i*asc, sep='')
            e = e + 1
            
        

            
        
    
    
    
