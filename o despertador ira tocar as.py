hora = int(input("Qual a hora atual? "))
faltam= int(input("Em quantas horas o despertador irá tocar? "))

v = (hora+faltam)%24
print("O despertador irá tocas à(s)", v, "h")
