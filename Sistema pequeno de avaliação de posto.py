contador1 = 0
contador2 = 0
contador3 = 0

while True:
    tipo = int(input("Digite o tipo de combustivel(1.Alcool)(2.Gasolina)(3.Disel)"))
    if tipo == 1:
        print ("Alcool")
        contador1 += 1
    elif tipo == 2:
        print ("Gasolina")
        contador2 += 1
    elif tipo == 3:
        print ("Dísel")
        contador3 += 1
    elif tipo == 4:
        print ("Fim")
        break
    else:
        print("Digite um valor existente")
print (contador1)
print (contador2)
print (contador3)


