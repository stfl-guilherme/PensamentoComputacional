'''
Você recebeu a lista com os campeões jogados por um player nas últimas 20 partidas:

campeoes = [
"Lux", "Ahri", "Lux", "Zed", "Yasuo", "Ahri", "Lux", "Vex", "Zed", "Ahri",
"Lux", "Lux", "Zoe", "Yone", "Ahri", "Vex", "Yasuo", "Lux", "Lux", "Ahri"
]

a) Escreva um programa que exiba quantas vezes cada campeão foi escolhido, sem utilizar dicionários.
b) Mostre o nome do campeão mais jogado.
'''

campeoes = [
"Lux", "Ahri", "Lux", "Zed", "Yasuo", "Ahri", "Lux", "Vex", "Zed", "Ahri",
"Lux", "Lux", "Zoe", "Yone", "Ahri", "Vex", "Yasuo", "Lux", "Lux", "Ahri"
]

contados = []
maisjogado = 0
contador = 0
maior = 0
mais = 0

for i in range(len(campeoes)):
    if contados not in campeoes:
        contados.append(campeoes[i])
    for j in range(len(campeoes)):
        if contados[i] == campeoes [j]:
            contador += 1

    if maior < contador:
        maior = contador
        mais = contados[i]
    print(contados[i], contador)
    contador = 0
print("mais jogado :",mais)