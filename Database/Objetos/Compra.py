class Compra:
    def __init__(self, codOperacao, cnpjFornecedor, cnpjRestaurante, notaFiscal, data, quantidade):
        self.codOperacao = codOperacao
        self.cnpjFornecedor = cnpjFornecedor
        self.cnpjRestaurante = cnpjRestaurante
        self.notaFiscal = notaFiscal
        self.data = data
        self.quantidade = quantidade

    def to_tuple(self):
        return (
            self.codOperacao,
            self.cnpjFornecedor,
            self.cnpjRestaurante,
            self.notaFiscal,
            self.data,
            self.quantidade
        )
