n = int(input('Digite um número menor que 46:'))
while n >= 46:
    n = int(input('Digite um número menor que 46:'))

lista = []

lista.append(0)
lista.append(1)
lista.append(1)

x = 2
while lista[x] < n:
    num = lista[x] + lista[x-1]
    lista.append(num)
    num = 0
    x += 1

lista.pop()
num_elementos = len(lista)
for i in range(0,num_elementos):
    print(lista[i])
