'''
Solicite 10 números inteiros ao usuário e armazene-os em uma lista. 
Depois, crie uma nova lista que contenha apenas os números que não são múltiplos de 3 e que também não são negativos. 
Exiba as duas listas: a original e a filtrada.
'''
def pedir(vetor):
    try:
        numero = int(input("digite o numero: "))
        vetor.append(numero)
        return vetor
    except:
        print("Digite um numero válido!")

def encher(vetor):
    m3 = []
    for i in range(len(vetor)):
        if vetor[i] % 3 == 0 and vetor[i] <= 30:
            m3.append(vetor[i])
    return m3

def main():
    vetor = []
    while len(vetor) < 10:
        vetor = pedir(vetor)
    m3 = encher(vetor)
    print("\nlista completa")
    print(vetor)
    print("\nmultiplos de 3")
    print(m3)
main()