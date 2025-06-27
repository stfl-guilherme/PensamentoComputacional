'''
Crie um programa que solicite ao usuário duas listas de 5 números cada. Em seguida, gere uma terceira
lista com 10 números aleatórios entre 8 e 25. Verifique se a soma dos valores das duas primeiras listas está
presente na terceira. (As listas informadas pelo usuário não podem conter números maiores que 10).
'''
import random

l1 = []
l2 = []
l3 = []

while len(l1) < 5:
    try:
        numero = int(input("Digite um número menor ou igual a 10: "))
        if numero <= 10:
            l1.append(numero)
    except:
        print("Digito inválido!")

while len(l2) < 5:
    try:
        numero2 = int(input("Digite um número menor ou igual a 10: "))
        if numero2 <= 10:
            l2.append(numero2)
        else:
            print("Número Inválido ou maior que 10!")
    except:
        print("Digito inválido!")

while len(l3) < 10:
    numero = random.randint(8, 25)
    l3.append(numero)

for i in range(len(l1)):
    soma = l1[i] + l2[i]
    if soma not in l3:
        print("não está na lista")
    else:
        print("está na lista")