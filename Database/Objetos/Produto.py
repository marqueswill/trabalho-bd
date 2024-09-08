class Produto:

    def __init__(
        self,
        nome=None,
        quantidade=None,
        unidade=None,
        descricao=None,
        codCategoria=None,
        codProduto=None,
    ):
        self.codProduto = codProduto
        self.unidade = unidade
        self.quantidade = quantidade
        self.nome = nome
        self.descricao = descricao
        self.codCategoria = codCategoria

    def __str__(self):
        return "Produto"

    def to_tuple(self):
        return (
            self.nome,
            self.quantidade,
            self.unidade,
            self.descricao,
            self.codCategoria,
            self.codProduto,
        )

    def columns(self):
        return [
            '"nome"',
            '"quantidade"',
            '"unidade"',
            '"descricao"',
            '"codCategoria"',
            '"codProduto"',
        ]

    def auto_columns(self):
        return [
            '"codProduto"',
        ]

    def keys(self):
        return [
            '"codProduto"',
        ]
