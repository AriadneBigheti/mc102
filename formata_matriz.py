def formata_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])-1):
            c = len(matriz[i])-1
            print(matriz[i][j], end=' ')
        print(matriz[i][c])
    return 
