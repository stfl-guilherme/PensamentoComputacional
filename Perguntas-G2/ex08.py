'''
Crie uma função chamada avaliar_kda que receba três listas do mesmo tamanho: abates, mortes e
assistencias. A função deve:
a) Calcular o KDA de cada partida com a fórmula: (abates + assistências) / max(1, mortes)
b) Retornar uma lista com os valores de KDA de cada partida.
'''
def avaliar_kda(abates, mortes, assis):
    kdas = []
    for i in range(len(abates)):
        kda = (abates[i] + assis[i]) / max(1, mortes[i])
        texto = f"Jogador {i + 1} - Pontuação KDA: {kda:.2f}"
        kdas.append(texto)
    return kdas

def main():
    abates = [3, 6, 4, 3, 2]
    mortes = [2, 1, 3, 4, 7]
    assis = [1, 8, 2, 1, 0]
    kdas = avaliar_kda(abates, mortes, assis)
    for i in range(len(kdas)):
        print(kdas[i])

main()