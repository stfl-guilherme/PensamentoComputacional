'''
Peça ao usuário para digitar duas sequências de 5 números e armazene-as em duas listas distintas. 
Em seguida, 
faça um programa que procure os elementos comuns entre elas e os junte em uma terceira lista.
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
for i in range(0, 5):
    if lista1[i] in lista2:
        lista3.append(lista1[i])
print(lista1)
print(lista2)
print(lista3)