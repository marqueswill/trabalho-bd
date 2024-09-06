from Database.Objetos import *
import os

categoria = Categoria()
compra = Compra()
cotacao = Cotacao()
entrada = Entrada()
estoque = Estoque()
fornecedor = Fornecedor()
funcionario = Funcionario()
inventario = Inventario()
lote = Lote()
produto_estoque = ProdutoEstoque()
produto_lote = ProdutoLote()
restaurante = Restaurante()
saida = Saida()

objects = {
    1: categoria,
    2: compra,
    3: cotacao,
    4: entrada,
    5: estoque,
    6: fornecedor,
    7: funcionario,
    8: inventario,
    9: lote,
    10: produto_estoque,
    11: produto_lote,
    12: restaurante,
    13: saida,
}


def linha():
    print("_" * 50)


def limpar():
    os.system("clear")


def TelaInicial():
    linha()
    print("Tela Inicial")
    linha()
    opcoes = {1: "CRUD", 2: "Sair"}
    for op in opcoes.items():
        print(f"{op[0]} - {op[1]}")
    # linha()
    try:
        escolha = int(input("Selecione uma opção: "))
    except ValueError:
        limpar()
        print("Entrada inválida, por favor, selecione uma opção válida.")
        return

    if escolha == 1:
        limpar()
        TelaEscolha()
    elif escolha == 2:
        limpar()
        exit()  # Use exit() to terminate the program
    else:
        print("Opção inválida, tente novamente.")
        linha()


def TelaEscolha():
    linha()
    print("Escolha uma Entidade")
    linha()
    for number, obj in objects.items():
        print(f"{number:>2} - {obj}")
    print("14 - Voltar")
    linha()
    try:
        escolha = int(input("Selecione uma entidade: "))
    except ValueError:
        limpar()
        print("Entrada inválida, por favor, selecione um número válido.")
        linha()
        return TelaEscolha()

    if escolha == 14:
        limpar()
        return TelaInicial()
    elif escolha not in objects:
        limpar()
        print("Entidade inválida, tente novamente.")
        linha()
        return TelaEscolha()

    TelaCRUD(objects[escolha])


def TelaCRUD(entidade):
    limpar()
    linha()
    print(f"CRUD de {entidade}")
    linha()

    opcoes = {1: "Criar", 2: "Ler", 3: "Atualizar", 4: "Deletar", 5: "Voltar"}
    for op in opcoes.items():
        print(f"{op[0]} - {op[1]}")
    # linha()
    try:
        escolha = int(input("Selecione uma operação: "))
    except ValueError:
        print("Entrada inválida, por favor, selecione uma opção válida.")
        linha()
        return

    if escolha == 1:
        TelaCreate(entidade)
    elif escolha == 2:
        TelaRead(entidade)
    elif escolha == 3:
        TelaUpdate(entidade)
    elif escolha == 4:
        TelaDelete(entidade)
    elif escolha == 5:
        return TelaEscolha()
    else:
        print("Opção inválida, tente novamente.")
        linha()


def TelaCreate(entidade):
    limpar()
    linha()
    print(f"Criando novo registro para {entidade}:")
    linha()


def TelaRead(entidade):
    limpar()
    linha()
    print(f"Lendo registros de {entidade}:")
    linha()


def TelaUpdate(entidade):
    limpar()
    linha()
    print(f"Atualizando registro de {entidade}:")
    linha()


def TelaDelete(entidade):
    limpar()
    linha()
    print(f"Deletando registro de {entidade}:")
    linha()


while True:
    TelaInicial()
