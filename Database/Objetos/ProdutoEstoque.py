class ProdutoEstoque:
    def __init__(
        self,
        codProduto,
        codEstoque,
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
