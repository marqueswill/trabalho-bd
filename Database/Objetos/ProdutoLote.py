class ProdutoLote:

    def __init__(
        self,
        quantidade=None,
        codProduto=None,
        codEstoque=None,
        numLote=None,
    ):
        self.quantidade = quantidade
        self.codProduto = codProduto
        self.codEstoque = codEstoque
        self.numLote = numLote

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

    def auto_columns(self):
        return []

    def keys(self):
        return [
            '"codProduto"',
            '"codEstoque"',
            '"numLote"',
        ]
