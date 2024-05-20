lista1 = []
np = []
n = int(input('Digite o tamanho da lista'))
v = 0
pares = 0

for i in range(1,n+1):
    v = int(input('Digite o valor'))
    lista1.insert(0,v)
    if (v % 2 == 0):
        np.append(v)

pares = (len(np) / len(lista1)) *100

print(len(lista1))
print(sum(lista1))

med = 0
total = sum(lista1)
contador=0

for c in range(0,n+1):
    contador+=1
    med = total/contador
print(med)
print(pares)
