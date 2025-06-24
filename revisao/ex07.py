'''
Peça ao usuário que digite 7 números inteiros e armazene-os em uma lista. 
O programa deve identificar o menor número da lista e o último número ímpar digitado, 
e calcular o produto entre eles. 
Exiba a lista, os dois valores encontrados e o resultado do produto.
'''
def encher(vetor):
    while len(vetor) != 10:
        try:
            numero = int(input("Digite um numero: "))
            vetor.append(numero)
        except:
            ("Digite um numero válido!")
    return vetor

def verificar(menor, u_impar, vetor):
    menor = vetor[0]
    for i in range(len(vetor)):
        if vetor[i] % 2 != 0:
            u_impar = vetor[i]
        if menor > vetor[i]:
            menor = vetor[i]
    return menor, u_impar

def conta(menor, u_impar):
    return (menor * u_impar)

def main():
    vetor = []
    menor = 0
    u_impar = 0
    vetor = encher(vetor)
    menor, u_impar = verificar(menor, u_impar, vetor)
    produto = conta(menor, u_impar)
    print("Lista Completa\n", vetor,"\nMenor número da lista\n",menor,"\nUltimo Digito impar da lista\n",u_impar,"\nProduto do ultimo impar e do menor número\n",produto)

main()