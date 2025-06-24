'''
Implemente o algoritmo conhecido como Crivo de Eratóstenes para encontrar todos os números primos de 2 até 100. 
Armazene os primos encontrados em uma lista e exiba-a ao final da execução.
'''
array = [2,]
for i in range(2, 101):
    if i % 1 == 0 and i % 2 != 0:
        array.append(i)
print("numeros primos de 2 a 100\n",array)