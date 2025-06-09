entregas = [
    "Ana - arroz - alimento - 03/06",
    "Bruno - sabão - higiene - 03/06",
    "Ana - feijão - alimento - 04/06",
    "Ana - arroz - alimento - 10/06",
    "Ana - arroz - alimento - 17/06",
    "Bruno - sabão - higiene - 17/06",
    "Bruno - sabão - higiene - 24/06",
    "Ana - máscara - higiene - 18/06",
    "Ana - casaco - roupa - 22/06",
    "Ana - boné - roupa - 25/06",
    "Ana - toalha - higiene - 28/06"
]

validas = []
invalidas = []
nomes = []
itens_recebidos = []
total_recebido = []

def processar_entregas():
    for registro in entregas:
        partes = registro.split(" - ")
        nome = partes[0]
        item = partes[1]
        categoria = partes[2]
        data = partes[3]

        if nome not in nomes:
            nomes.append(nome)
            itens_recebidos.append([item])
            total_recebido.append(1)
            validas.append(registro)
        else:
            indice = nomes.index(nome)
            qtd_item = itens_recebidos[indice].count(item)

            if total_recebido[indice] >= 5:
                invalidas.append(registro + " - motivo: excedeu limite total")
            elif qtd_item >= 2:
                invalidas.append(registro + " - motivo: excedeu limite do item")
            else:
                itens_recebidos[indice].append(item)
                total_recebido[indice] += 1
                validas.append(registro)

def relatorio_por_morador():
    for i in range(len(nomes)):
        print(f"\nMorador: {nomes[i]}")
        print("Entregas válidas:")
        contador = 0
        for registro in validas:
            partes = registro.split(" - ")
            if partes[0] == nomes[i]:
                print(f"- {partes[1]} ({partes[2]}), recebido em {partes[3]}")
                contador += 1
        print(f"Total de itens recebidos: {contador}")

def relatorio_invalidas():
    print("\nEntregas inválidas:")
    for registro in invalidas:
        partes = registro.split(" - ")
        print(f"{partes[0]} - {partes[1]} - {partes[-1]}")

def resumo_geral():
    print("\nResumo Geral:")
    print("Total de moradores atendidos:", len(nomes))

    maximo = max(total_recebido)
    for i in range(len(nomes)):
        if total_recebido[i] == maximo:
            print("Morador que mais recebeu:", nomes[i], f"({maximo} itens válidos)")

    print("Total de entregas inválidas:", len(invalidas))

def adicionar_entrega():
    print("\nAdicionar nova entrega:")
    nome = input("Nome do morador: ")
    item = input("Nome do item: ")
    categoria = input("Categoria (alimento, higiene, roupa): ")
    data = input("Data (ex: 10/06): ")
    nova_entrega = f"{nome} - {item} - {categoria} - {data}"
    entregas.append(nova_entrega)
    print("Entrega adicionada com sucesso!")


def menu():
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-") 
    print("-=-=-=-PREFEITURA-DE-VALE-VERDE-=-=-=-")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    print("<1>PROCESSAR_ENTREGAS<->")
    print("<2>RELATÓRIO_POR_MORADOR<->")
    print("<3>RELATÓRIO_ENTREGAS_INVÁLIDAS<->")
    print("<4>RESUMO_GERAL<->")
    print("<5>ADICIONAR_ENTREGA<->")
    print("<6>SAIR<->")

def main():
    while True:
        menu()
        op = input("Escolha uma opção: ")
        if op == "1":
            processar_entregas()
        elif op == "2":
            relatorio_por_morador()
        elif op == "3":
            relatorio_invalidas()
        elif op == "4":
            resumo_geral()
        elif op == "5":
            adicionar_entrega()
        elif op == "6":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()
