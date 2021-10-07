lista = []
n = int(input("Digite:"))
while n < 0:
    n = int(input("Digite:"))
fim_da_lista = int(((n - (n%2))/2)+1)

for x in range (1,fim_da_lista):
    y = 2*x
    lista.append(y)
    lista[x-1] = str(lista[x-1])

lista = ' '.join(lista)
print(lista)








