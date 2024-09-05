class Ajuste:
    def __init__(
        self,
        valorAntigo,
        valorNovo,
        diferenca,
        codProduto,
        codEstoque,
        dataInv,
    ):
        self.valorAntigo = valorAntigo
        self.valorNovo = valorNovo
        self.diferenca = diferenca
        self.codProduto = codProduto
        self.codEstoque = codEstoque
        self.dataInv = dataInv

    def to_tuple(self):
        return (
            self.valorAntigo,
            self.valorNovo,
            self.diferenca,
            self.codProduto,
            self.codEstoque,
            self.dataInv,
        )

    def columns(self):
        return [
            "valorAntigo",
            "valorNovo",
            "diferenca",
            "codProduto",
            "codEstoque",
            "dataInv",
        ]