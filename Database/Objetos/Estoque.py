class Estoque:

    def __init__(self, codEstoque=None, nome=None, cnpjRestaurante=None):
        self.codEstoque = codEstoque
        self.nome = nome
        self.cnpjRestaurante = cnpjRestaurante

    def __str__(self):
        return "Estoque"

    def to_tuple(self):
        return (
            self.codEstoque,
            self.nome,
            self.cnpjRestaurante,
        )

    def columns(self):
        return [
            '"codEstoque"',
            '"nome"',
            '"cnpjRestaurante"',
        ]
