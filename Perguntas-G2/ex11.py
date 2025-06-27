'''
Crie um menu simples de um caixa eletrônico com as opções: sacar, depositar, ver saldo, extrato de
transações e sair. A função main() deve conter apenas as chamadas de funções e as estruturas if.
'''
def menu():
    print("menu")
    print("sacar")
    print("depositar")
    print("saldo")
    print("extrato")
    print("sair")
    opc = int(input("digite a opc: "))
    return opc

def sacar(saldo,extrato):
    saque = float(input("Digite a quantida que deseja sacar: "))
    if saque <= saldo:
        saldo -= saque
        texto = f"Saque efetuado no valor de {saque}"
        extrato.append(texto)
    else:
        print("valor insuficiente")
    return saldo, extrato

def depositar(saldo,extrato):
    dep = float(input("Digite a quantida que deseja sacar: "))
    saldo += dep
    texto = f"deposito efetuado no valor de {dep}"
    extrato.append(texto)
    return saldo, extrato

def mostrar(saldo):
    print(saldo)

def monstrarextrato(extrato):
    for i in range(len(extrato)):
        print(extrato[i])

def main():
    saldo = 0
    opc = 0
    extrato = []
    while opc != 5:
        opc = menu()
        if opc == 1:
            saldo, extrato = sacar(saldo,extrato)
        elif opc == 2:
            saldo, extrato = depositar(saldo,extrato)
        elif opc == 3:
            mostrar(saldo)
        elif opc == 4:
            monstrarextrato(extrato)

main()