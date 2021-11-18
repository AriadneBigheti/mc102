i = 0
soma = 0 
caracois_0 = 0
caracois_1 = 0
caracois_2 = 0
d = 0
maior_tempo= 0
menor_tempo= 0

while i!=(-1):
    i = int(input())
    if i!=(-1):
        d = d + 1
        soma = soma + i
    
        if i < 180:
            caracois_0 = caracois_0 + 1
        elif 180 <= i < 240:
            caracois_1 = caracois_1 + 1
        else:
            caracois_2 = caracois_2 + 1

        if d>1 and i>maior_tempo:
            maior_tempo = i
        elif d>1 and i<=menor_tempo:
            menor_tempo = i
        elif d==1:
            maior_tempo = i
            menor_tempo = i

def tempo_medio(x , y):
    return format(x/y, '.1f') 
def velocidade_media(y):
    return format(33/(y/60), '.1f')
    
print("Caracois no nivel 0:", caracois_0)
print("Caracois no nivel 1:", caracois_1)
print("Caracois no nivel 2:", caracois_2)
print("Tempo medio:", tempo_medio(soma,d), "s")
print("Velocidade maxima:", velocidade_media(menor_tempo), "cm/min")
print("Velocidade minima:", velocidade_media(maior_tempo), "cm/min")      

