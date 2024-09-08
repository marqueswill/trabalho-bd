class Inventario:
    def __init__(
        self,
        contagem=None,
        diferenca=None,
        ajustado=None,
        cpfEstoquista=None,
        codProduto=None,
        codEstoque=None,
        data=None,
    ):
        self.contagem = contagem
        self.diferenca = diferenca
        self.ajustado = ajustado
        self.cpfEstoquista = cpfEstoquista
        self.codProduto = codProduto
        self.codEstoque = codEstoque
        self.data = data

    def __str__(self):
        return "Inventario"

    def to_tuple(self):
        return (
            self.contagem,
            self.diferenca,
            self.ajustado,
            self.cpfEstoquista,
            self.codProduto,
            self.codEstoque,
            self.data,
        )

    def columns(self):
        return [
            '"contagem"',
            '"diferenca"',
            '"ajustado"',
            '"cpfEstoquista"',
            '"codProduto"',
            '"codEstoque"',
            '"data"',
        ]

    def auto_columns(self):
        return [
            '"diferenca"',
        ]

    def keys(self):
        return [
            '"codProduto"',
            '"codEstoque"',
            '"data"',
        ]
