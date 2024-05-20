segundos = int(input("Coloque o tempo em segundos: "))
minutos = round (segundos/60)
segundos = round (segundos%60)
hora = round (minutos/60)
minutos = round (minutos%60)

print("Horas  Minutos  Segundos", hora, minutos, segundos)
