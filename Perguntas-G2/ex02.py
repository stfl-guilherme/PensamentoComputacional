'''
Crie um programa em Python que solicite ao usuário a digitação de 5 números inteiros (um por vez). Em
seguida, armazene esses números em uma lista e, ao final, exiba a lista completa e o maior valor presente
nela.
'''
maior = 0
lista = []
while len(lista) <5:
    try:
        numero = int(input("Digite um número: "))
        lista.append(numero)
    except:
        print("numero inválido")
maior = lista[0]
for i in range(len(lista)):
    if maior < lista[i]:
        maior = lista[i]

print(lista)
print(maior)