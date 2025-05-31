def cadastrar_aluno(nomes,idades):
    print("\n=============CADASTRO=============")
    print("=|Digite_o_nome_do_aluno|=")
    nome = input("")
    nomes.append(nome)
    print("=|Digite_a_idade_do_aluno|=")
    try:
        idade= int(input(""))
        idades.append(idade)
    except:
        print("==idade_inválida==")
        nomes.pop()
    print("==================================\n")
    print("|=>Aperte_enter_para_continuar<=|")
    input()
    return nomes,idades

def listar_aluno(nomes,idades):
    print("\n=================================")
    for i in range(len(nomes)):
        print(i + 1,".",nomes[i], idades[i],"anos")
    print("=================================\n")
    print("|=>Aperte_enter_para_continuar<=|")
    input()

def maior_de_18(nomes,idades):
    numero = 1
    print("\n=================================")
    for i in range(len(idades)):
        if idades[i] >= 18:
            print(numero,".",nomes[i], idades[i],"anos")
            numero += 1
    print("=================================\n")
    print("|=>Aperte_enter_para_continuar<=|")
    input()

def remover_participantes(nomes,idades):
    print("\n=================================")
    print("=>Digite_o_nome_do_participante_que_você_deseja_remover<=")
    nome = input(":")
    i = 0
    contador = 0
    while i < len(nomes):
        if nomes[i] == nome:
            nomes.pop(i)
            idades.pop(i)
            contador = contador + 1
        else:
            i = i + 1
    if contador == 0:
        print("=>nome_não_encontrado!<=")
    print("=================================\n")
    print("|=>Aperte_enter_para_continuar<=|")
    input()
    return nomes,idades

def estat(nomes, idades):
    numero = 0
    soma = 0
    maior = 0
    print("\n=================================")
    for i in range (len(nomes)):
        numero += 1
        soma += idades[i]
        if i == 0:
            maior = idades[i]
        if idades[i] > maior:
            maior = idades[i]
    print("=>Estatísticas<=")
    print("Total_de_participantes_registrados:", numero)
    print("Média das idades_registradas:", soma/numero)
    for i in range(len(idades)):
        if idades[i] == maior:
            print("Nome_e_idade_do_participante_mais_velho:", nomes[i], idades[i]," anos e está na posição", i + 1," da lista")
    print("=================================\n")
    print("|=>Aperte_enter_para_continuar<=|")
    input()

def menu():
    print("===================================")
    print("==========MENU_DE_CADASTRO=========")
    print("=>1.Cadastrar_aluno")
    print("=>2.Listar_alunos")
    print("=>3.Participantes_maiores_de_Idade")
    print("=>4.Remover_participante")
    print("=>5.Mostrar_estátiscas")
    print("=>6.Sair")
    print("===================================")


def main():
    nomes = []
    idades = []
    opc = 0
    while opc != 6:
        menu()
        opc = int(input("\nDigite_a_Opção_desejada: \n"))
        if opc == 1:
            cadastrar_aluno(nomes, idades)
        elif opc == 2:
            listar_aluno(nomes,idades)
        elif opc == 3:
            maior_de_18(nomes,idades)
        elif opc == 4:
            remover_participantes(nomes,idades)
        elif opc == 5:
            estat(nomes,idades)
        elif opc == 6:
            print("Obrigado!")
        elif opc <= 0 or opc > 6:
            print("\n==Opção_Errada==\n")

main()
