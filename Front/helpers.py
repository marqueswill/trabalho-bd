import os
import pandas as pd
from tabulate import tabulate

from Database.Objetos import *
from Database.Integracao import *

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
    10: DBProduto(),
    11: DBProdutoEstoque(),
    12: DBProdutoLote(),
    13: DBRestaurante(),
    14: DBSaida(),
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


def listar(entidade):
    registros = entidade.get_all()

    headers = [c.replace('"', "") for c in objetos[str(entidade)].columns()]
    valores = {}
    for h in headers:
        valores[h] = []
    for l in registros:
        col = l.to_tuple()
        for i in range(len(col)):
            valores[headers[i]].append(col[i])

    df = pd.DataFrame(valores)

    df.reset_index(drop=True, inplace=True)

    print(tabulate(df, headers="keys", tablefmt="psql", showindex=True))

    return registros


def selecionar(entidade, escolha):
    registros = entidade.get_all()
    dic = {}
    for i in range(len(registros)):
        dic[i] = registros[i]
    return dic[int(escolha)]


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
        "ProdutoLote": ProdutoLote,
        "ProdutoEstoque": ProdutoEstoque,
        "Restaurante": Restaurante,
        "Saida": Saida,
    }

    cls = entidades.get(str(entidade))
    print(valores)
    for i, v in enumerate(valores):
        if v:
            if str(v).lower() == "true":
                valores[i] = True
            elif str(v).lower() == "false":
                valores[i] = False

    print(valores)
    if cls:
        return cls(*valores)
    else:
        raise ValueError(f"Entidade {entidade} não reconhecida.")
