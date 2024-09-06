class ProdutoEstoque:

    def __init__(
        self,
        codProduto=None,
        codEstoque=None,
        estoqueMax=None,
        estoqueMin=None,
        estoqueAtual=None,
        estoqueDisp=None,
        ultimoInv=None,
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
            self.codProduto,
            self.codEstoque,
            self.estoqueMax,
            self.estoqueMin,
            self.estoqueAtual,
            self.estoqueDisp,
            self.ultimoInv,
        )

    def columns(self):
        return [
            "'codProduto'",
            "'codEstoque'",
            "'estoqueMax'",
            "'estoqueMin'",
            "'estoqueAtual'",
            "'estoqueDisp'",
            "'ultimoInv'",
        ]
