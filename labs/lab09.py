def tupla(x):
    x = x[1:-1]
    x = x.split(",")
    f = float (x[0])
    i = int (x[1])
    return (f,i)

notas_lab = [tupla(x) for x in input().split()]

notas_prova = [float(x) for x in input().split()]

exame = -1

m_lab = 0
divisor = 0

for i in range(len(notas_lab)):
    m_lab += (notas_lab[i][0])*(notas_lab[i][1])
    divisor += notas_lab[i][1]
    
m_lab = m_lab/divisor

m_prova = (notas_prova[0]*3 + notas_prova[1]*4)/7

if m_prova>=5 and m_lab>=5:
    m_final = 0.7*m_prova + 0.3*m_lab
    aprovado = True
    
elif m_prova>=2.5 and m_lab>=2.5:
    exame = float(input())
    m_preliminar = min(4.9, 0.7*m_prova + 0.3*m_lab)
    m_final = (m_preliminar + exame)/2
    
    if m_final>=5.0:
        aprovado = True
    else:
        aprovado = False
else:
    m_final = min(m_prova, m_lab)
    aprovado = False
    

print("Media das tarefas de laboratorio:" , format(m_lab, '.1f'))
print("Media das provas:" , format(m_prova, '.1f'))

if exame != -1:  
    print("Media preliminar:" , format(m_preliminar, '.1f'))
    print("Nota no exame:", format(exame, '.1f'))

if aprovado:
    print("Aprovado(a) por nota e frequencia")
else:
    print("Reprovado(a) por nota")

print("Media final:" , format(m_final, '.1f'))
