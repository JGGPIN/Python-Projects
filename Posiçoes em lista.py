lista = []
n = int(input("Entre com o tamanho da lista: "))
for i in range (n):
    x = int(input("Entre com os numeros: "))
    lista.append(x)
print(lista)
y = (min(lista))
print(f"Menor valor {y}")
print(f"Posição {lista.index(y)}")
