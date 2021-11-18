massa = float(input())
idade = int(input())
if 16<idade<18:
    documento = input()    
sintomas = input()
viagem = input()
contato_covid = input()
primeira_doacao = input()
if primeira_doacao == "N":
    doacoes_12meses = int(input())
    if doacoes_12meses>0 :
        meses_ultimadoacao = int(input())        
sexo = input()
if sexo == "F" :
    gravida_amamentando = input()                


print("Massa corporal:", massa)
print("Idade:", idade)
if 16<idade<18:
    print("Documento de autorizacao:", documento)
print("Febre ou sintomas gripais:", sintomas)
print("Viagem recente ao exterior:", viagem)
print("Contato com caso de COVID-19:", contato_covid)
print("Primeira doacao:", primeira_doacao)
if primeira_doacao == "N":
    print("Doacoes nos ultimos 12 meses:", doacoes_12meses)                      
    if doacoes_12meses>0:
        print ("Meses desde ultima doacao:", meses_ultimadoacao)
print("Sexo biologico:", sexo)
if sexo == "F" :
    print("Gravida ou amamentando:", gravida_amamentando)



if massa < 50.0:
    print("Impedimento: abaixo da massa corporal minima")
    v = (1>2)
else:
    v = (2>1)
    
if idade < 16 :
    print("Impedimento: menor de 16 anos")
    v = v and (1>2)
elif 16<idade<18 and documento == "N":
    print("Impedimento: menor de 18 anos sem consentimento dos responsaveis")
    v = v and (1>2)
elif 60<idade<69 and primeira_doacao == "S":
    print ("Impedimento: maior de 60 anos e primeira doacao")
    v = v and (1>2)
elif idade>69:
    print ("Impedimento: maior de 69 anos")
    v = v and (1>2)
    
if sintomas == "S":
    print("Impedimento: febre ou sintomas gripais")
    v = v and (1>2)
    
if viagem == "S":
    print("Impedimento: viagem recente ao exterior")
    v = v and (1>2)

if contato_covid =="S":
    print("Impedimento: contato com caso de COVID-19")
    v = v and (1>2)

if primeira_doacao =="N" and doacoes_12meses>0:
    if sexo == "M":
        if doacoes_12meses>=4:
            print("Impedimento: numero maximo de doacoes anuais foi atingido")
            v = v and (1>2)

        if meses_ultimadoacao<2:
            print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")
            v = v and (1>2)

    else:
        if doacoes_12meses>=3:
            print("Impedimento: numero maximo de doacoes anuais foi atingido")
            v = v and (1>2)

        if meses_ultimadoacao<3:
            print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")
            v = v and (1>2)

if sexo =="F" and gravida_amamentando == "S":
    print("Impedimento: gravida ou amamentando")
    v = v and (1>2)

if v == (2>1):
    print("Agende um horario para triagem completa")
            
