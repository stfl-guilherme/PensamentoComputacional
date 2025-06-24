'''
Solicite ao usuário um número inteiro positivo.
Gere a sequência de Collatz a partir desse número: 
se for par, divide por 2; se for ímpar, multiplica por 3 e soma 1. 
Continue até que o número chegue a 1. Armazene todos os valores da sequência em uma lista e exiba-a.
'''
def gerar():
    numero = -1
    while numero <= -1:
        numero = int(input("Digite um número: "))
    return numero

def collatz(numero):
    lista = []
    while numero != 1:
        if numero % 2 == 0:
            numero /= 2
        else:
            numero *= 3
            numero += 1
        lista.append(numero)
    return lista

def main():
    numero = gerar()
    lista = collatz(numero)
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=\n=>Número Digitado\n",numero,"\n=>Lista dos termos da sequência Collatz\n",lista)
main()