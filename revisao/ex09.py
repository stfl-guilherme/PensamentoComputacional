'''
Crie um programa que recebe um valor n do usuário e encontra os primeiros n números perfeitos. 
Um número é considerado perfeito quando a soma dos seus divisores próprios (excluindo ele mesmo) é igual a ele. 
Por exemplo, 6 é perfeito pois 1 + 2 + 3 = 6. Exiba os números perfeitos encontrados. 
Dica: Não tente descobrir o quinto número perfeito ou maior :)
'''
n = -1
lista = []
contador = 0
num = 1  

while n <= 0:
    try:
        print("Digite quantos números perfeitos deseja encontrar:")
        n = int(input())
    except:
        print("Digite um número válido!")

while contador < n:
    soma = 0
    for i in range(1, num):
        if num % i == 0:
            soma += i
    if soma == num:
        lista.append(num)
        contador += 1
    num += 1

print("\nNúmeros perfeitos encontrados:")
print(lista)
#usei chat para interpretar, não tava entendendo a busca por numeros perfeitos