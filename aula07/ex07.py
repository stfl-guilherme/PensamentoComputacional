'''
 Peça ao usuário para digitar uma sequência de 10 números. Em seguida, crie duas listas a partir desta sequência: 
 uma contendo os números pares e outra contendo os números ímpares.
'''
listap = []
listai = []
for i in range(0,10):
    numero = int(input("Digite um numero: "))
    if numero%2==0:
        listap.append(numero)
    else:
        listai.append(numero)
print("listaa dos impar: ", listai)
print("lista dos pares: ",listap)