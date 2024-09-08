class Inventario:
    def __init__(
        self,
        codProduto=None,
        codEstoque=None,
        data=None,
        contagem=None,
        diferenca=None,
        ajustado=None,
        cpfEstoquista=None,
    ):
        self.codProduto = codProduto
        self.codEstoque = codEstoque
        self.data = data
        self.contagem = contagem
        self.diferenca = diferenca
        self.ajustado = ajustado
        self.cpfEstoquista = cpfEstoquista

    def __str__(self):
        return "Inventario"

    def to_tuple(self):
        return (
            self.codProduto,
            self.codEstoque,
            self.data,
            self.contagem,
            self.diferenca,
            self.ajustado,
            self.cpfEstoquista,
        )

    def columns(self):
        return [
            '"codProduto"',
            '"codEstoque"',
            '"data"',
            '"contagem"',
            '"diferenca"',
            '"ajustado"',
            '"cpfEstoquista"',
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
