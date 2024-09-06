class Compra:
    def __init__(self, codOperacao, cnpjFornecedor, cnpjRestaurante, notaFiscal, data):
        self.codOperacao = codOperacao
        self.cnpjFornecedor = cnpjFornecedor
        self.cnpjRestaurante = cnpjRestaurante
        self.notaFiscal = notaFiscal
        self.data = data
        #self.quantidade = quantidade

    def to_tuple(self):
        return (
            self.data,
            self.notaFiscal,
            self.codOperacao,
            self.cnpjFornecedor,
            self.cnpjRestaurante,
            #self.quantidade
        )
