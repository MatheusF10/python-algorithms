
numerox1 = float(input("Digite a coordenada x"))
numeroy1 = float(input("Digite a coordenada y"))
pontox2 = float(input("Digite a coordenada de outro ponto x"))
pontoy2 = float(input("Digite a coordenada de outro ponto y"))
import math 
dab = math.sqrt((numerox1 - numeroy1)**2 + (pontox2 - pontoy2)**2)

if dab >= 10:
    print("longe")
else:
    print("perto")
    
    
