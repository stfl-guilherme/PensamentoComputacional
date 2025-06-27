def separar_pares_impares():
    numeros = []
    pares = []
    impares = []

    for i in range(10):
        n = int(input(f"Digite o {i+1}º número inteiro: "))
        numeros.append(n)
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    
    return pares, impares

def somar_lista(lista):
    soma = 0
    for valor in lista:
        soma += valor
    return soma