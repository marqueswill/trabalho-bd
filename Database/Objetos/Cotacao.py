class Cotacao:
    def __init__(self, valor, codProduto, cnpjFornecedor):
        self.valor = valor
        self.codProduto = codProduto
        self.cnpjFornecedor = cnpjFornecedor

    def to_tuple(self):
        return (
            self.valor,
            self.codProduto,
            self.cnpjFornecedor,
        )
