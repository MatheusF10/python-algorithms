import math

a = int(input("Digite o valor de a"))
b = int(input("Digite o valor de b"))
c = int(input("Digite o valor de c"))


delta = (b*b) - (4*a*c)


if delta < 0:
    print("esta equação não possui raízes reais")
elif delta == 0:
     X = (-1*b + math.sqrt(delta)) / (2*a)
     print("a raiz desta equação é", X)
elif delta > 0:
         X = (-1*b + math.sqrt(delta)) / (2*a)
         Y = (-1*b - math.sqrt(delta)) / (2*a)
         print("as raízes da equação são", Y, "e", X)
    
            
            
         
         
         
