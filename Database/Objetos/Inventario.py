class Inventario:
    def __init__( self, codProduto, codEstoque, dataInv, diferenca, ajustado, contagem=None, cpfEstoquista=None):
        self.codProduto = codProduto
        self.codEstoque = codEstoque
        self.dataInv = dataInv
        self.contagem = contagem
        self.diferenca = diferenca
        self.ajustado = ajustado
        self.cpfEstoquista = cpfEstoquista

    def to_tuple(self):
        return (
            self.codProduto,
            self.codEstoque,
            self.dataInv,
            self.contagem,
            self.diferenca,
            self.ajustado,
            self.cpfEstoquista,
        )
