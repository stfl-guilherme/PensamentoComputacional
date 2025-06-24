'''
Solicite que o usuário digite 12 números inteiros. 
Em seguida, peça mais um número para busca. 
O programa deve informar a última posição (índice) em que esse número apareceu na lista. 
Caso o número não esteja presente, uma mensagem adequada deve ser exibida.
'''
vetor = []

while len(vetor) != 12:
    try:
        valor = int(input("Digite o seu valor: "))
        vetor.append(valor)
    except:
        print("Resposta Inválida!")

valor = int(input("Digite o valor para checar: "))
for i in range(11, -1, -1):
    if vetor[i] == valor:
        print("O seu valor é", valor,"e está presente na lista na posição",(i + 1))
        break
    else:
        print("valor não encontrado")
        break