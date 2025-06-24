'''
Escreva um programa que solicite ao usuário que digite 10 números inteiros, um por vez.
Armazene esses valores em uma lista. Depois, percorra a lista e calcule a soma de todos os números pares.
Ao final, exiba a lista completa e o valor da soma dos pares.
'''
numeros = []
soma = 0

while len(numeros) <= 10:
    numero = int(input("Digite um numero: "))
    numeros.append(numero)

for i in range (len(numeros)):
    if numeros[i] % 2 == 0:
        soma += numeros[i]

print(numeros)
print(soma)
