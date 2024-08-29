class ProdutoLote:
    def __init__(self, codProduto, codEstoque, numLote):
        self.codProduto = codProduto
        self.codEstoque = codEstoque
        self.numLote = numLote

    def to_tuple(self):
        return (self.codProduto, self.codEstoque, self.numLote)
