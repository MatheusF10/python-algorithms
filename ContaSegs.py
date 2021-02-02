segundos = input ("Por favor, entre com o número de segundos que deseja converter: ")
totalsegs = int (segundos)

dias = totalsegs // 86400
seg_restantes1 = totalsegs % 86400
horas = seg_restantes1 // 3600
seg_restantes = totalsegs % 3600
minutos = seg_restantes // 60
seg_restantes_final = seg_restantes % 60

print (dias, "dias, ", horas, "horas, ", minutos, "minutos e", seg_restantes_final, "segundos.")
