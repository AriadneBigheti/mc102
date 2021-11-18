valor = float(input())
dias_atraso = int(input())

print("Valor: R$", format(valor, '.2f'))

multa = valor * 0.02
print("Multa: R$", format(multa, '.2f'))

juros = 0.00033 * valor * dias_atraso
print("Juros: R$", format(juros, '.2f'))

valor_total = valor + multa + juros
print("Valor total: R$", format(valor_total, '.2f'))

valor_min = valor_total * 0.1
print("Valor minimo para renegociacao: R$", format(valor_min, '.2f'))                        
