def soma_matriz(m1, m2):
    m3=[]
    for i in range(len(m1)):
        soma =[]
        for j in range(len(m1[1])):
            soma.append(m1[i][j]+m2[i][j])
        m3.append(soma)
    return m3
        
