class Inventario:
    def __init__(
        self,
        codProduto,
        codEstoque,
        data,
        contagem,
        diferenca,
        ajustado,
        cpfEstoquista,
    ):
        self.codProduto = codProduto
        self.codEstoque = codEstoque
        self.data = data
        self.contagem = contagem
        self.diferenca = diferenca
        self.ajustado = ajustado
        self.cpfEstoquista = cpfEstoquista

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
