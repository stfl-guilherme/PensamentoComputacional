def adicionar_lista(lista):
    tarefa = input("Escreva a nova tarefa para adicionar: ")
    lista.append(tarefa)
    return lista

def lista_tarefas(lista,listac):
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("==Lista_das_Tarefas_Pendentes==")
    for i in range(len(lista)):
        print(">",(i + 1), lista[i])
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("==Lista_das_Tarefas_Concluidas==")
    for i in range(len(listac)):
        print(">",i + 1,". ",listac[i])
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    return lista, listac
def concluir_tarefa(lista,listac):
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("==Lista_das_Tarefas_Pendentes==")
    for i in range(len(lista)):
        print(">",(i + 1), lista[i])
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    try:
        tarefa = int(input("Digite a tarefa que deseja concluir: "))
        resposta = tarefa - 1
        for i in range(len(lista)):
            if i == resposta:
                listac.append(lista[i] + " \u2705")
                lista.pop(resposta)
    except:
        print("==Digite_Um_Número_Presente_Na_Lista==")
    return listac, lista

def editar_lista(lista):
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("==Lista_das_Tarefas_Pendentes==")
    for i in range(len(lista)):
        print(">",(i + 1), lista[i])
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    try:
        tarefa = int(input("Digite o número da tarefa que você deseja editar: "))
        edicao = input("Digite o novo texto: ")
        tarefa -= 1
        for i in range(len(lista)):
            if i == tarefa:
                lista.pop(i)
                lista.insert(i, edicao)
    except:
        print("==Digite_Um_Número_Presente_Na_Lista==")
    return lista

def excluir_tarefa(lista):
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("==Lista_das_Tarefas_Pendentes==")
    for i in range(len(lista)):
        print(">",(i + 1), lista[i])
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    try:
        tarefa = int(input("Digite o número da tarefa que você deseja excluir: "))
        tarefa -= 1
        for i in range(len(lista)):
            if i == tarefa:
                lista.pop(i)
    except:
        print("==Digite_Um_Número_Presente_Na_Lista==")
    
    return lista

def mostar(lista,listac):
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("==Obrigado_Aqui_Está_Sua_Lista==")
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("==Lista_das_Tarefas_Pendentes==")
    for i in range(len(lista)):
        print(">",(i + 1), lista[i])
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("==Lista_das_Tarefas_Concluidas==")
    for i in range(len(listac)):
        print(">",i + 1,". ",listac[i])
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")


def main():
    lista = []
    listac = []
    menu = 0
    while menu != 6:
        print("-+-+MENU_DE_TAREFAS-+-+")
        print("[1] Adicionar nova tarefa")
        print("[2] Listar tarefas")
        print("[3] Concluir tarefa")
        print("[4] Editar tarefa pendente")
        print("[5] Excluir tarefa pendente")
        print("[6] Sair")
        menu = int(input("Digite a opção que você deseja: "))
        if menu == 1:
            adicionar = adicionar_lista(lista)
        elif menu == 2:
            listar = lista_tarefas(lista,listac)
        elif menu == 3:
            concluir = concluir_tarefa(lista,listac)
        elif menu == 4:
            editar = editar_lista(lista)
        elif menu == 5:
            excluir = excluir_tarefa(lista)
        elif menu == 6:
            me = mostar(lista,listac)
        elif menu <= 0 or menu > 6:
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("====Digite_Uma_Opção_Válida====")
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
main ()