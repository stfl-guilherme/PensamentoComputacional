numero1 = 0
numero2 = 1
sequencia = 0

termos = int(input("Quantos termos da sequência fibonacci você deseja ver: "))
while sequencia != termos:
    numeroX = numero1 + numero2
    numero1 = numero2
    numero2 = numeroX 
    sequencia += 1
    print(numero1)