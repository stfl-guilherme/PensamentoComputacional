'''
10. Crie uma lista com 10 posições. Em seguida, crie uma função para cada uma das situações abaixo:
• Adicionar valores à lista
• Retornar apenas os números pares da lista
• Alterar o valor de uma posição solicitada pelo usuário
'''
def adicionar(lista):
    numero = int(input("Digite o numero: "))
    lista.append(numero)
    return lista

def eh_par(lista, pares):
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            pares.append(lista[i])
    return pares

def alterar_valor(lista):
    pos = int(input("Digite uma posição pra trocar: "))
    numero = int(input("novo número: "))
    lista.pop(pos)
    lista.insert(pos, numero)
    return lista

def main():
    lista = []
    while len(lista) < 10:
        lista = adicionar(lista)
    pares = []
    pares = eh_par(lista, pares)
    lista = alterar_valor(lista)
    print(lista)
    print(pares)

main()
