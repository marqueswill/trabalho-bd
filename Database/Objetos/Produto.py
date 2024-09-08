class Produto:

    def __init__(
        self,
        codProduto=None,
        unidade=None,
        quantidade=None,
        nome=None,
        descricao=None,
        codCategoria=None,
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
            self.unidade,
            self.quantidade,
            self.nome,
            self.descricao,
            self.codCategoria,
            self.codProduto,
        )

    def columns(self):
        return [
            '"unidade"',
            '"quantidade"',
            '"nome"',
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
