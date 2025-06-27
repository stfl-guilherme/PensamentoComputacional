'''
12. Crie uma função que gere 10 números inteiros aleatórios entre 0 e 100, sem repetições. Adicione à lista
apenas os números pares. Em seguida, exiba o menor e o maior valor da lista.
'''
import random

def funcao(lista):
    while len(lista) < 10:
        numero = random.randint(0, 100)
        if numero % 2 == 0 and numero not in lista:
            lista.append(numero)
    maior = menor = lista[0]
    for i in range(1, len(lista)):
        if maior < lista[i]:
            maior = lista[i]
        if menor > lista[i]:
            menor = lista[i]
    print("menor: ",menor )
    print("maior: ",maior)
    return lista

def main():
    lista = []
    lista = funcao(lista)
    print(lista)
main()