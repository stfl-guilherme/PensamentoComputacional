'''
Você foi contratado para programar o sistema de um cofrinho digital para ajudar crianças a controlarem suas economias. Cada vez que uma criança guarda um valor, esse valor é registrado em uma lista. O sistema precisa oferecer um menu com as seguintes opções:

=== Cofrinho Digital ===
1. Adicionar valor ao cofrinho
2. Ver todos os valores guardados
3. Ver o total economizado
4. Ver quantas vezes um valor específico foi guardado
5. Retirar o valor mais recente adicionado
6. Sair

O sistema deve funcionar em um laço while, exibindo o menu após cada operação, até que o usuário escolha a opção 6 para sair.
A opção 1 deve solicitar um valor positivo e adicioná-lo à lista.
A opção 2 exibe todos os valores guardados, na ordem em que foram adicionados.
A opção 3 calcula e exibe a soma total dos valores guardados.
A opção 4 deve solicitar um valor ao usuário e contar quantas vezes ele aparece na lista.
A opção 5 remove o último valor adicionado (se houver) e informa qual foi removido.
'''

def menu():
    print("\n=== Cofrinho Digital ===")
    print("1. Adicionar valor ao cofrinho")
    print("2. Ver todos os valores guardados")
    print("3. Ver o total economizado")
    print("4. Ver quantas vezes um valor específico foi guardado")
    print("5. Retirar o valor mais recente adicionado")
    print("6. Sair")

def main():
    cofre = []
    opcao = 0

    while opcao != 6:
        menu()
        try:
            opcao = int(input("Escolha uma opção: "))
        except:
            print("Digite um número válido!")
            continue

        if opcao == 1:
            valor = float(input("Digite o valor a guardar (positivo): "))
            if valor > 0:
                cofre.append(valor)
                print(f"R${valor:.2f} adicionado ao cofrinho!")
            else:
                print("Valor inválido! Só pode guardar valores positivos.")

        elif opcao == 2:
            if cofre:
                print("Valores guardados:")
                for v in cofre:
                    print(f"R${v:.2f}")
            else:
                print("O cofrinho está vazio.")

        elif opcao == 3:
            total = sum(cofre)
            print(f"Total economizado: R${total:.2f}")

        elif opcao == 4:
            busca = float(input("Digite o valor a procurar: "))
            quantidade = cofre.count(busca)
            print(f"O valor R${busca:.2f} foi guardado {quantidade} vez(es).")

        elif opcao == 5:
            if cofre:
                removido = cofre.pop()
                print(f"O valor R${removido:.2f} foi retirado do cofrinho.")
            else:
                print("O cofrinho está vazio. Nada a remover.")

        elif opcao == 6:
            print("Saindo... Até a próxima! 🐷")

        else:
            print("Opção inválida! Tente novamente.")

main()