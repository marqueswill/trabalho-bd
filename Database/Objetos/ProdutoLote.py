class ProdutoLote:

    def __init__(self, codProduto=None, codEstoque=None, numLote=None, quantidade=None):
        self.codProduto = codProduto
        self.codEstoque = codEstoque
        self.numLote = numLote
        self.quantidade = quantidade

    def __str__(self):
        return "ProdutoLote"

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
