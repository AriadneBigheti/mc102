import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

def delta (x, y, z):
   return (y**2 - (4*x*z))

def raiz_delta (a, b, c):
   return math.sqrt(delta(a, b, c))

if delta(a, b, c)< 0:
   print("Não existem raizes reais")
else:
   def r1():
      return(-b + raiz_delta(a, b, c))/(2*a)
   def r2():
      return(-b - raiz_delta(a, b, c))/(2*a)

   if delta(a, b, c) ==0:
      print("Existe uma raiz real: ", r1())

   else:
      print("Existem duas raizes reais: ", r1(), "e", r2())
   
