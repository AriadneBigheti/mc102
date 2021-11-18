valor = float(input("Digite o valor da transação: "))

if valor<= 0:
    print("Valor inválido")
    
elif valor<=2500.00:
    c = 30 + valor*0.017
    if c>39.00:
         print("O valor da comissão é: R$", format(c, '.2f'))
    else:
         print("O valor da comissão é: R$", 39.00)

elif 2500.01<=(valor)<=6250.00:
    c = 56 + valor*0.0066
    print("O valor da comissão é: R$", format(c, '.2f'))
     
elif 6251.01<=(valor)<=20000.00:
     c = 76 + valor*0.0034
     print("O valor da comissão é: R$", format(c, '.2f'))

elif 20000.01<=(valor)<=50000.00:
     c = 100 + valor*0.0022
     print("O valor da comissão é: R$", format(c, '.2f'))

elif 50000.01<=(valor)<=500000.00:
     c = 155 + valor*0.0011
     print("O valor da comissão é: R$", format(c, '.2f'))

else:     
     c = 255 + valor*0.0009
     print("O valor da comissão é: R$", format(c, '.2f'))
