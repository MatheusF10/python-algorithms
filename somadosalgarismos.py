numint = int(input("Digite um número inteiro: "))

soma = 0

while numint > 0:
    resto = numint % 10
    numint = (numint - resto) // 10
    soma = soma + resto
print(soma)
     
