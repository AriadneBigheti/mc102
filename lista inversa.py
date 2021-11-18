v = 1
sequencia = []
numeros = []

while v!=0:
    v = int(input())
    sequencia.append(v)

tamanho = len(sequencia)
x = 1

while x<=tamanho:
    numeros.append(sequencia[tamanho - x])
    x = x + 1

print(numeros)
