v1 = int(input("Entre com o primeiro valor"))
v2 = int(input("Entre com o segundo valor"))
v3 = int(input("Entre com o terceiro valor"))

t = str(input("Escolha o tipo de avaliação"))

ma = (v1 + v2 + v3)/3
mp = (v1*5 + v2*3 + v3*2)/10


if t == 'a' or 'A':
        print("O valor equivale a ", ma)

elif t == 'p' or 'P':
         print("o valor equivale a ", mp)

else:
        print("Opção inválida")



