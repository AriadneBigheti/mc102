def compara(a,b,precisao=1e-5):
    return (abs(a-b) <= precisao)

def raiz_quadrada(n):
    ini=1
    fim=n
    meio = (ini+fim)/2
    while not compara(meio**2, n):
        if n <= meio**2:
            fim = meio
        elif n > meio**2:
            ini = meio
        meio = (ini+fim)/2
    return meio

        
            
        
    
    
            
            
        
        
