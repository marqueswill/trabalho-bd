from Database.Objetos import *
from Database.Integracao import *
import os
import pandas as pd
from tabulate import tabulate
from Database.Integracao.DBOperation import DBOperation

db = DBOperation()
db.setup()

entitites = {
    1: DBCategoria(),
    2: DBCompra(),
    3: DBCotacao(),
    4: DBEntrada(),
    5: DBEstoque(),
    6: DBFornecedor(),
    7: DBFuncionario(),
    8: DBInventario(),
    9: DBLote(),
    10: DBProdutoEstoque(),
    11: DBProdutoLote(),
    12: DBRestaurante(),
    13: DBSaida(),
}

objetos = {
    "Categoria": Categoria(),
    "Compra": Compra(),
    "Cotacao": Cotacao(),
    "Entrada": Entrada(),
    "Estoque": Estoque(),
    "Fornecedor": Fornecedor(),
    "Funcionario": Funcionario(),
    "Inventario": Inventario(),
    "Lote": Lote(),
    "ProdutoEstoque": ProdutoEstoque(),
    "ProdutoLote": ProdutoLote(),
    "Restaurante": Restaurante(),
    "Saida": Saida(),
}


def linha():
    print("+" * 50)


def limpar():
    os.system("clear")


def TelaInicial():
    limpar()

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

        print("Entrada inválida, por favor, selecione uma opção válida.")
        return

    if escolha == 1:
        TelaEscolha()
    elif escolha == 2:
        exit()  # Use exit() to terminate the program
    else:
        print("Opção inválida, tente novamente.")
        linha()


def TelaEscolha():
    limpar()
    linha()
    print("Escolha uma Entidade")
    linha()
    print(" 0 - Voltar\n")
    for number, e in entitites.items():

        print(f"{number:>2} - {e}")
    linha()
    try:
        escolha = int(input("Selecione uma entidade: "))
    except ValueError:

        print("Entrada inválida, por favor, selecione um número válido.")
        linha()
        return TelaEscolha()

    if escolha == 0:

        return TelaInicial()
    elif escolha not in entitites:

        print("Entidade inválida, tente novamente.")
        linha()
        return TelaEscolha()

    TelaCRUD(entitites[escolha])


import pandas as pd


def listar(entidade):
    linhas = entidade.get_all()

    headers = [c.replace('"', "") for c in objetos[str(entidade)].columns()]
    valores = {}
    for h in headers:
        valores[h] = []
    for l in linhas:
        col = l.to_tuple()
        for i in range(len(col)):
            valores[headers[i]].append(col[i])

    df = pd.DataFrame(valores)

    df.reset_index(drop=True, inplace=True)

    print(tabulate(df, headers="keys", tablefmt="psql", showindex=True))

    return


def selecionar(entidade, escolha):
    linhas = entidade.get_all()

    registros = {}
    for i in range(len(linhas)):
        registros[i] = linhas[i]
    return registros[int(escolha)]


def TelaCRUD(entidade):
    limpar()

    linha()
    print(f"CRUD de {entidade}")
    linha()

    opcoes = {
        0: "Voltar\n",
        1: "Criar",
        2: "Ler",
        3: "Atualizar",
        4: "Deletar",
    }
    for op in opcoes.items():
        print(f"{op[0]} - {op[1]}")
    try:
        escolha = int(input("Selecione uma operação: "))
    except ValueError:
        print("Entrada inválida, por favor, selecione uma opção válida.")
        linha()
        return

    if escolha == 0:
        return TelaEscolha()
    elif escolha == 1:
        TelaCreate(entidade)
    elif escolha == 2:
        TelaRead(entidade)
    elif escolha == 3:
        TelaUpdate(entidade)
    elif escolha == 4:
        TelaDelete(entidade)

    else:
        print("Opção inválida, tente novamente.")
        linha()


def generate_object(entidade, valores):
    entidades = {
        "Categoria": Categoria,
        "Cotacao": Cotacao,
        "Compra": Compra,
        "Entrada": Entrada,
        "Estoque": Estoque,
        "Fornecedor": Fornecedor,
        "Funcionario": Funcionario,
        "Inventario": Inventario,
        "Lote": Lote,
        "Produto": Produto,
        "ProdutoEstoque": ProdutoEstoque,
        "Restaurante": Restaurante,
        "Saida": Saida,
    }

    cls = entidades.get(str(entidade))
    if cls:
        return cls(*valores)
    else:
        raise ValueError(f"Entidade {entidade} não reconhecida.")


def TelaCreate(entidade):
    limpar()

    linha()
    print(f"Criando novo registro para {entidade}:")
    linha()

    valores = []
    for col in objetos[str(entidade)].columns():
        valores.append(input(col.replace('"', "") + ": "))

    try:
        obj = generate_object(entidade, valores)
        entidade.insert(obj)
        
        input("Registro inserido com sucesso!")
        return TelaCRUD(entidade)
    except:
        opcao = input("Não foi possível atualizar o registro! Deseja continuar? (S/N)")
        if opcao.lower() in ["s", "y"]:
            return TelaCreate(entidade)
        else:
            return TelaCRUD(entidade)
        pass
    return


def TelaRead(entidade):
    limpar()

    linha()
    print(f"Lendo registros de {entidade}:")
    linha()
    listar(entidade)
    linha()

    try:
        escolha = int(input("Aperte qualquer tecla para voltar"))
        return TelaCRUD(entidade)
    except ValueError:
        return TelaCRUD(entidade)


def TelaUpdate(entidade):
    limpar()
    linha()
    listar(entidade)
    linha()
    escolha = input("Selecione o registro que deseja atualizar: ")

    linha()

    try:
        selecionado = selecionar(entidade, escolha)

        valores = []
        for c in selecionado.columns()[:-1]:
            valores += input(c.replace('"', "") + ": ")
        print(f"Atualizando registro de {entidade}")
        atualizado = entidade.generate(valores)
        entidade.update(atualizado)
    except:
        input("Não foi possível atualizar o registro!")
        return TelaDelete(entidade)

    input("Registro atualizar com sucesso!")
    return TelaCRUD(entidade)


def TelaDelete(entidade):
    limpar()
    linha()
    listar(entidade)
    linha()
    escolha = input("Selecione o registro que deseja deletar: ")

    linha()

    try:
        selecionado = selecionar(entidade, escolha)
        print(f"Deletando registro de {entidade}")
        entidade.delete(selecionado)
    except:
        input("Não foi possível deletar o registro!")
        return TelaDelete(entidade)

    input("Registro deletado com sucesso!")
    return TelaCRUD(entidade)


while True:
    TelaInicial()
