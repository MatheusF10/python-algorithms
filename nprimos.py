num= int(input("Digite um número inteiro"))
contador = 1

while contador <= num:
    if num%2 == 1:
        contador = contador+1
        print("Primo")
        break
    else:
        print("não primo")
        break
