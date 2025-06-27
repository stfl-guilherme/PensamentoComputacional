'''
18. Crie um sistema que receba 10 números inteiros, armazene-os em uma lista e, em seguida, gere uma
nova lista apenas com os números que não se repetem e são divisíveis por 5.
'''
lista = []
lista2 = []
while len(lista) < 10:
    try:
        numero = int(input("Digite um numero"))
        lista.append(numero)
        if numero not in lista2 and numero % 5 == 0:
            lista2.append(numero)
    except:
        print("Digito errado")
print(lista)
print(lista2)