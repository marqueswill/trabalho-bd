class Estoque:
    def __init__(self, codEstoque, nome, cnpjRestaurante):
        self.codEstoque = codEstoque
        self.nome = nome
        self.cnpjRestaurante = cnpjRestaurante

    def to_tuple(self):
        return (
            self.codEstoque,
            self.nome,
            self.cnpjRestaurante,
        )
