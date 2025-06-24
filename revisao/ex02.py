'''
Peça ao usuário que informe 10 números inteiros e armazene-os em uma lista.
Em seguida, crie uma nova lista contendo apenas os números que são quadrados perfeitos
, ou seja, aqueles cuja raiz quadrada é um número inteiro exato. Para verificar isso no Python,
você pode usar a função math.sqrt() para calcular a raiz quadrada.
'''
import math

numeros = []
quadrados_perfeitos = []

for i in range(10):
    valor = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(valor)

for n in numeros:
    if n >= 0:
        raiz = math.sqrt(n)
        if raiz == int(raiz):
            quadrados_perfeitos.append(n)

print("\nNúmeros digitados:")
print(numeros)
print("\nQuadrados perfeitos encontrados:")
print(quadrados_perfeitos)
#usei chat, não entendi o que extamente o import math faz