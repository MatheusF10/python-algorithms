tamArq = int(input("Digite o tamanho do arquivo"))
velLink = float(input("Digite a velocidade do link"))

Mbps = velLink * 8
temdown = Mbps * tamArq // 60

print("a velocidade de download e", Mbps, "sera concluido em" , temdown ,"minutos")


             
