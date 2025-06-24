'''
Peça ao usuário que digite 5 números inteiros para formar a primeira lista e, em seguida, mais 5 números para formar a segunda lista. 
Em seguida, calcule todas as somas possíveis entre os elementos das duas listas, combinando cada número da primeira com cada número da segunda. 
Armazene em uma nova lista apenas as somas que forem números pares, garantindo que cada valor apareça apenas uma vez. 
Ao final, exiba a lista contendo todas as somas pares distintas geradas a partir das combinações.
'''
array1 = []
array2 = []
array3 = []

while len(array1) < 5:
    print("Digite um número para a primeira lista:")
    numero = int(input())
    array1.append(numero)

while len(array2) < 5:
    print("Digite um número para a segunda lista:")
    numero = int(input())
    array2.append(numero)

for i in range(len(array1)):
    for j in range(len(array2)):
        soma = array1[i] + array2[j]
        if soma % 2 == 0 and soma not in array3:
            array3.append(soma)

print("\nPrimeira lista:")
print(array1)
print("\nSegunda lista:")
print(array2)
print("\nSomas pares distintas:")
print(array3)