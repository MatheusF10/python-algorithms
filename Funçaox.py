def Funçao_x():
  import math 
  import matploblib.pyplot
  numero1 = int(input("digite o numero da função"))
  numero2 = int(input("digite o numero da função"))
  x1 = math.sqrt(numero1)
  x2 = math.sqrt(numero2)
  f = (x1 - numero1) * (x2 + numero2)
  matploblib.pyplot.plot(f)
