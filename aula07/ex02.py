temperaturas = [30,22,25,28,31,27,29]
print(temperaturas)
tamanho = len(temperaturas)
numero = 0
for i in range(tamanho):
    if temperaturas[i] < 25:
        temperaturas[i] += 5
print(temperaturas)