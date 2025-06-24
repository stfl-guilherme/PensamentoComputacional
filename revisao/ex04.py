'''
Peça ao usuário para digitar as notas de 8 alunos e armazene-as em uma lista. 
Depois, calcule a média da turma e exiba apenas as notas que estão acima da média,
indicando que esses alunos tiveram desempenho acima do esperado.
'''
notas = []
soma = 0
nomes = []

while len(notas) != 8:
    try:
        nome = input("Digite seu nome: ").upper()
        nota = int(input("Digite a sua nota: "))
        if nota >= 0 or nota <= 10:
            notas.append(nota)
            nomes.append(nome)
        else:
            print("Nota Inválida!")
    except:
        print("Resposta Inválida!")
print("=-=-=-=-=-=-=-=-=-=-=-=-=")
print("=-=-ALUNOS=-DESTAQUES-=-=")
print("=-=-=-=-=-=-=-=-=-=-=-=-=")
for i in range(len(notas)):
    soma += notas[i]
    if notas[i] >= 7:
        print("=>NOME:", nomes[i])
        print("=>NOTA:", notas[i])
print("=-=-=-=-=-=-=-=-=-=-=-=-=")
print("-=-=-=MÉDIA=DA-TURMA=-=-=")
print("=>MÉDIA: ", soma/len(notas))
print("=-=-=-=-=-=-=-=-=-=-=-=-=")