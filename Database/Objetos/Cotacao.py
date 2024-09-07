class Cotacao:

    def __init__(self, valor=None, codProduto=None, cnpjFornecedor=None):
        self.valor = valor
        self.codProduto = codProduto
        self.cnpjFornecedor = cnpjFornecedor

    def __str__(self):
        return "Cotacao"

    def to_tuple(self):
        return (
            self.valor,
            self.codProduto,
            self.cnpjFornecedor,
        )

    def columns(self):
        return [
            '"valor"',
            '"codProduto"',
            '"cnpjFornecedor"',
        ]
