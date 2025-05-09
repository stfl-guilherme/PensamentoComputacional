'''
Peça ao usuário para digitar uma sequência de 10 números.
Após, procure o maior e o menor número e apresente na tela.
'''
sequencia = []
maior = 0
menor = 0
for i in range(0, 10):
    numero = int(input("Digite seu numero: "))
    sequencia.append(numero)
    maior = menor = sequencia[0]

    for i in range(1, len(sequencia)):
        if maior < sequencia[i]:
            maior = sequencia[i]
        if menor > sequencia[i]:
            menor = sequencia[i]
print(menor,maior)