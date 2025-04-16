tentativas = 0

while tentativas <= 3:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario != "admin" and senha != 1234:
        print("Usuário ou senha incorretos.")
        tentativas +=1
    else:
        print("Acesso liberado!")
        tentativas = 4

    if tentativas == 3:
        print("Conta Bloqueada, Tente novamente mais tarde")
        tentativas += 1
