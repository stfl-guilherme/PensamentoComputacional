'''
Peça ao usuário para digitar as idades de várias pessoas, até o usuário digitar o valor 0.
Após, calcule a média das idades e apresente na tela.
'''
idades = []
idade = -1
soma = 0
print("Digite 0 para sair")
while idade != 0:
    idade = int(input("Digite a idade: "))
    idades.append(idade)
    soma += idade
tamanho = len(idades)
tamanho -= 1

print("A média é :", soma / tamanho)