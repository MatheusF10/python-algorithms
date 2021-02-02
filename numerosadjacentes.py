n = int(input("Digite um número inteiro"))

anterior = n%10

n = n // 10

adjiguais  = False

pos = 0

while n > 0 and not adjiguais:
    atual = n % 10
    if atual == anterior:
        adjinguais = True
        print("Sim")
        break
    else:
        print("Não")
        break
        
    
    
    

