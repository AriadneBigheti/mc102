matriz =[]
matriz.append([ x for x in input()])
t = ""

while t != "+":
    i = [ x for x in input()]
    matriz.append(i)
    t = i[0]
 
num_quadros = int(input())
matriz_2 = [s.copy() for s in matriz]

def formata_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])-1):
            c = len(matriz[i])-1
            print(matriz[i][j], end='')
        print(matriz[i][c])
    return 

formata_matriz(matriz)

#sobrevivência - 2 ou 3 vizinhos
#morte - >=4 vizinhos ou <2 vizinhos

v=0
for n in range(num_quadros):
    for i in range(1,len(matriz)-1):
        for j in range(1, len(matriz[1])-1):
            #elemento matriz[i][j]:
            if matriz[i][j-1] == "@":
                v+=1
            if matriz[i][j+1] == "@":
                v+=1
            if matriz[i-1][j] == "@":
                v+=1
            if matriz[i-1][j-1] == "@":
                v+=1
            if matriz[i-1][j+1] == "@":
                v+=1
            if matriz[i+1][j] == "@":
                v+=1
            if matriz[i+1][j-1] == "@":
                v+=1
            if matriz[i+1][j+1] == "@":
                v+=1
        
            if matriz[i][j] == "@":
                if v>=4 or v<2:
                    matriz_2[i][j] = " "

            elif matriz[i][j] == " ":
                if v==3:
                    matriz_2[i][j] = "@"
            v=0
    formata_matriz(matriz_2)
    matriz = [s.copy() for s in matriz_2]


    
                   
    
            
                   
    
 
