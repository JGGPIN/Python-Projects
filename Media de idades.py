contador = 0
somaidade = 0

while True:
    idade = int(input("Digite sua idade (ou -1 para encerrar): "))
    if idade == -1:
        break
    somaidade += idade
    contador += 1

if contador > 0:
    mediaidade = somaidade / contador
    print("A média de idade é:", mediaidade)
    print("A soma das idades é:", somaidade)
else:
    print("Nenhuma idade foi inserida.")
