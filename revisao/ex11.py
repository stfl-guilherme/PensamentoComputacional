'''
Peça ao usuário para informar uma base (número inteiro) e um expoente máximo.
Crie uma função que retorna uma lista com todas as potências da base, 
do expoente 0 até o máximo informado. 
Exiba essa lista.
'''
numero = int(input("Digite um número: "))
expoente = int(input("Digite um expoente maximo: "))
lista = []
for i in range(0, expoente + 1):
    conta = numero ** i
    lista.append(conta)
    print(lista)
print(lista)