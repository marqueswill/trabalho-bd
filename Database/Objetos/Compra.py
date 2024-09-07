class Compra:

    def __init__(
        self,
        codOperacao=None,
        cnpjFornecedor=None,
        cnpjRestaurante=None,
        notaFiscal=None,
        data=None,
    ):
        self.codOperacao = codOperacao
        self.cnpjFornecedor = cnpjFornecedor
        self.cnpjRestaurante = cnpjRestaurante
        self.notaFiscal = notaFiscal
        self.data = data

    def __str__(self):
        return "Compra"

    def to_tuple(self):
        return (
            self.codOperacao,
            self.cnpjFornecedor,
            self.cnpjRestaurante,
            self.notaFiscal,
            self.data,
        )

    def columns(self):
        return [
            '"codOperacao"',
            '"cnpjFornecedor"',
            '"cnpjRestaurante"',
            '"notaFiscal"',
            '"data"',
        ]
