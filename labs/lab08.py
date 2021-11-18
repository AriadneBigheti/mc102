lista = input().split()
palavras = []
numeros = []
hashtags = []
emoticons = []

for i in range(0, len(lista)):
    
    if lista[i].isalpha():
        palavras.append(lista[i])
        
    elif lista[i].isdigit() or (lista[i][:1] == "-" and lista[i][1:].isdigit()):
        numeros.append(lista[i])
        
    elif (lista[i][:1] == "#") and (lista[i][1:].isalpha()):
        hashtags.append(lista[i])

    else:
        emoticons.append(lista[i])

if len(palavras)!=0:
    print("Palavra(s):", end=' ')
    for p in range (0, len(palavras)-1):
        print(palavras[p], end=' ')
    print(palavras[len(palavras) - 1])   
else:
    print("Palavra(s):")
    
if len(numeros)!=0:
    print("Numero(s):", end=' ')
    for n in range(0, len(numeros)-1):
        print(numeros[n], end=' ')
    print(numeros[len(numeros) - 1])
else:
    print("Numero(s):")

    
if len(hashtags)!=0:
    print("Hashtag(s):", end=' ')
    for h in range(0, len(hashtags)-1):
        print(hashtags[h], end=' ')
    print(hashtags[len(hashtags) - 1])
else:
    print("Hashtag(s):")
    
if len(emoticons)!=0:
    print("Emoticon(s):", end=' ')
    for e in range(0, len(emoticons)-1):
        print(emoticons[e], end=' ')
    print(emoticons[len(emoticons) - 1])
else:
    print("Emoticon(s):")
