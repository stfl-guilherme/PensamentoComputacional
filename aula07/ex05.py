'''
Peça ao usuário para digitar duas sequências de 5 números e armazene em duas listas distintas.
Após, faça um programa que junte essas duas listas em uma só.
'''
lista1 = []
lista2 = []
lista3 = []
for i in range(0, 5):
    numero = int(input("Digite o numero da primeira sequencia: "))
    lista1.append(numero)
for i in range(0, 5):
    numero = int(input("Digite o numero da segunda sequencia: "))
    lista2.append(numero)
for i in range(0, len(lista1)):
    lista3.append(lista1[i])
for i in range(0, len(lista2)):
    lista3.append(lista2[i])

print(lista1)
print(lista2)
print(lista3)