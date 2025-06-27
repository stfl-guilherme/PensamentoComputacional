'''
Crie um programa em Python que contenha uma função chamada somar, que receba dois números,
realize a soma e retorne o resultado. Peça ao usuário dois números, chame a função e exiba o resultado da
soma.
'''
def somar(n1,n2):
    return n1 + n2

def main():
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite um número: "))
    resultado = somar(n1,n2)
    print (resultado)
main()
