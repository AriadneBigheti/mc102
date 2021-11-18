def multiplica_matriz(m1,m2):
    m3=[]
    for i in range(len(m1)):
        linha=[]
        for n in range(len(m2[1])):
            multiplicacao=0
            for j in range(len(m2)):
                multiplicacao += (m1[i][j])*(m2[j][n])
            linha.append(multiplicacao)
        m3.append(linha)
    return m3
        
            
                   
