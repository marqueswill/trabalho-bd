class ProdutoLote:

    def __init__(self, codProduto, codEstoque, numLote, quantidade):
        self.codProduto = codProduto
        self.codEstoque = codEstoque
        self.numLote = numLote
        self.quantidade = quantidade

    def to_tuple(self):
        return (
            self.quantidade,
            self.codProduto,
            self.codEstoque,
            self.numLote,
        )

    def columns(self):
        return [
            '"quantidade"',
            '"codProduto"',
            '"codEstoque"',
            '"numLote"',
        ]
