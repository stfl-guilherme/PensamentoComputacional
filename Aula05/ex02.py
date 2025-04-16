menu = 1
troco = 0
total = 0
pagamento = 0

while menu != 0:
    total = int(input("Digite o valor total da compra: "))
    pagamento = int(input("Digite o valor pago: "))
    troco = pagamento - total

    if pagamento == total or pagamento >= total:
        nota100 = troco // 100
        troco %= 100
        nota50 = troco // 50
        troco %= 50
        nota20 = troco // 20
        troco %= 20
        nota10 = troco // 10
        troco %= 10
        nota5 = troco // 5
        troco %= 5
        nota2 = troco // 2
        troco %= 2 
        print("Total de notas para o troco")
        print("Notas de 100R$: ", nota100)
        print("Notas de 50R$: ", nota50)
        print("Notas de 20R$: ", nota20)
        print("Notas de 10R$: ", nota10)
        print("Notas de 5R$: ", nota5)
        print("Notas de 2R$: ", nota2)
    else:
        print("Valor insufieciente. Tente Novamente.")