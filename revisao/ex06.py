'''
Implemente um programa que gere os 15 primeiros números da sequência de Fibonacci. 
Utilize uma lista para armazenar os valores gerados e exiba a lista completa ao final. 
A sequência começa com 0 e 1, e cada número seguinte é a soma dos dois anteriores.
'''
a = 0
b = 1
c = 0
lista = []
for i in range(15):
    lista.append(a)
    c = a + b
    a = b
    b = c
print(lista)