class ProdutoEstoque:

    def __init__(
        self,
        estoqueMax=None,
        estoqueMin=None,
        estoqueAtual=None,
        estoqueDisp=None,
        ultimoInv=None,
        codProduto=None,
        codEstoque=None,
    ):
        self.codProduto = codProduto
        self.codEstoque = codEstoque
        self.estoqueMax = estoqueMax
        self.estoqueMin = estoqueMin
        self.estoqueAtual = estoqueAtual
        self.estoqueDisp = estoqueDisp
        self.ultimoInv = ultimoInv

    def __str__(self):
        return "ProdutoEstoque"

    def to_tuple(self):
        return (
            self.estoqueMax,
            self.estoqueMin,
            self.estoqueAtual,
            self.estoqueDisp,
            self.ultimoInv,
            self.codProduto,
            self.codEstoque,
        )

    def columns(self):
        return [
            '"estoqueMax"',
            '"estoqueMin"',
            '"estoqueAtual"',
            '"estoqueDisp"',
            '"ultimoInv"',
            '"codProduto"',
            '"codEstoque"',
        ]

    def auto_columns(self):
        return [
            '"estoqueMax"',
            '"estoqueMin"',
            '"estoqueAtual"',
            '"estoqueDisp"',
            '"ultimoInv"',
        ]

    def keys(self):
        return [
            '"codProduto"',
            '"codEstoque"',
        ]
