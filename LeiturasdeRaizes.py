import math

a = float(input("Digite o valor de a"))

b = float(input("Digite o valor de b"))

c = float(input("Digite o valor de c"))

delta = b**2 - 4 * a * c

if delta == 0:
    raizx = (-b + math.sqrt(delta)) / (2 * a)
    print("A raiz desta equaçao e", raizx)
    else:
        raizx = (-b + math.sqrt(delta)) / (2 * a)
        raizy = (-b - math.sqrt(delta)) / (2 * a)
        print("A raiz desta equação é", raizx)
        print("A raiz desta equação é", raizy)
        

raizx = (-b + math.sqrt(delta)) / (2 * a)
raizy = (-b - math.sqrt(delta)) / (2 * a)

    
print("A primeira raiz é:", raizx)
print("A segunda raiz é :", raizy)



          
