v = input()
usuarios = {}
while v!="--": 
    usuarios.update({v:[]}) #criação de um dicionario em que key=nome do usuario, value=lista de amigos
    v = input()

t = input().split()
while t[0]!= "--" :
    for i in usuarios.keys():
        if (i) == t[0]: #então t[1] é seu amigo
            usuarios[i].append(t[1])
        if (i) == t[1]: #então t[0] é seu amigo
            usuarios[i].append(t[0])
        usuarios[i].sort()
    t = input().split()
      
nomes=[]
for i in usuarios.keys():
        nomes.append((i))
nomes.sort()
        

lista = nomes[:]
for i in range(len(nomes)):
    lista.remove(nomes[i]) #remove seu nome para comparar com os outros usuarios
    if lista != []:
        for j in range(len(lista)):
            g = nomes[i]+" "+lista[j] #comparação de usuarios
            h = list(set(usuarios[nomes[i]]).intersection(usuarios[lista[j]])) #intersecção das listas de amigos
            h.sort()
            if h!=[]:
                k =""
                for x in range(len(h)-1):
                    k += h[x] + ", "
                k+=h[len(h)-1]
                print(g,":",k)
            else: #se nao há amigos em comum
                print(g,":")

