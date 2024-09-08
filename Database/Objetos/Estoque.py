class Estoque:

    def __init__(
        self,
        nome=None,
        cnpjRestaurante=None,
        codEstoque=None,
    ):
        self.nome = nome
        self.codEstoque = codEstoque
        self.cnpjRestaurante = cnpjRestaurante

    def __str__(self):
        return "Estoque"

    def to_tuple(self):
        return (
            self.nome,
            self.cnpjRestaurante,
            self.codEstoque,
        )

    def columns(self):
        return [
            '"nome"',
            '"cnpjRestaurante"',
            '"codEstoque"',
        ]

    def auto_columns(self):
        return [
            '"codEstoque"',
        ]

    def keys(self):
        return [
            '"codEstoque"',
        ]
