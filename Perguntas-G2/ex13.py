'''
Crie uma função que receba duas listas com 10 números inteiros aleatórios (sem repetições de 0 a 100).
Depois, some os respectivos elementos das duas listas e crie uma nova lista apenas com os resultados
pares. O programa deve exibir cada soma realizada.
'''
import random

def somar(l1, l2, l3):
    for i in range(len(l1)):
        soma = l1[i] + l2[i]
        texto = f"Soma realiza: {l1[i]} + {l2[i]} = {soma}"
        print(texto)
        if soma % 2 == 0:
            l3.append(soma)
    return l3

def encher(l):
    numero = random.randint(0, 100)
    if numero not in l:
        l.append(numero)
    return l

def main():
    l1 = []
    l2 = []
    l3 = []
    while len(l2) < 10:
        l1 = encher(l1)
        l2 = encher(l2)
    l3 = somar(l1, l2, l3)
    print(l1)
    print(l2)
    print(l3)
main()
