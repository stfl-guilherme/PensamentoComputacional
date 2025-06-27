'''
Crie um código que encontre e exiba a maior e a menor palavra de uma lista, considerando o número
de caracteres.
'''
lista = ["ornitorinco","banana", "limão", "abacate", "kiwi"]
maior = menor = (len(lista[0]))
maior_p = menor_p = ""
for i in range(len(lista)):
    if maior <= len(lista[i]):
        maior = len(lista[i])
        maior_p = lista[i]
    if menor >= len(lista[i]):
        menor = len(lista[i])
        menor_p = lista[i]
print(lista)
print("maior palavra: ", maior_p)
print("menor palavra: ", menor_p)
