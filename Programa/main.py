from Database.Objetos import *
from Database.Integracao import *
import os

# teste
categoria, db_categoria = Categoria(), DBCategoria()
compra, db_compra = Compra(), DBCompra()
cotacao, db_cotacao = Cotacao(), DBCotacao()
entrada, db_entrada = Entrada(), DBEntrada()
estoque, db_estoque = Estoque(), DBEstoque()
fornecedor, db_fornecedor = Fornecedor(), DBFornecedor()
funcionario, db_funcionario = Funcionario(), DBFuncionario()
inventario, db_inventario = Inventario(), DBInventario()
lote, db_lote = Lote(), DBLote()
produto_estoque, db_produto_estoque = ProdutoEstoque(), DBProdutoEstoque()
produto_lote, db_produto_lote = ProdutoLote(), DBProdutoLote()
restaurante, db_restaurante = Restaurante(), DBRestaurante()
saida, db_saida = Saida(), DBSaida()

entitites = {
    1: {"obj": categoria, "conn": db_categoria},
    2: {"obj": compra, "conn": db_compra},
    3: {"obj": cotacao, "conn": db_cotacao},
    4: {"obj": entrada, "conn": db_entrada},
    5: {"obj": estoque, "conn": db_estoque},
    6: {"obj": fornecedor, "conn": db_fornecedor},
    7: {"obj": funcionario, "conn": db_funcionario},
    8: {"obj": inventario, "conn": db_inventario},
    9: {"obj": lote, "conn": db_lote},
    10: {"obj": produto_estoque, "conn": db_produto_estoque},
    11: {"obj": produto_lote, "conn": db_produto_lote},
    12: {"obj": restaurante, "conn": db_restaurante},
    13: {"obj": saida, "conn": db_saida},
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
    for number, e in entitites.items():

        print(f"{number:>2} - {e['obj']}")
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
    elif escolha not in entitites:
        limpar()
        print("Entidade inválida, tente novamente.")
        linha()
        return TelaEscolha()

    TelaCRUD(entitites[escolha])


def TelaCRUD(entidade):
    limpar()
    linha()
    print(f"CRUD de {entidade['obj']}")
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
