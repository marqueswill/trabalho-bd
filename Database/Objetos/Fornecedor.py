class Fornecedor:

    def __init__(
        self,
        endereco=None,
        razao=None,
        nome=None,
        telefone=None,
        cnpjFornecedor=None,
    ):
        self.endereco = endereco
        self.razao = razao
        self.nome = nome
        self.telefone = telefone
        self.cnpjFornecedor = cnpjFornecedor

    def __str__(self):
        return "Fornecedor"

    def to_tuple(self):
        return (
            self.endereco,
            self.razao,
            self.nome,
            self.telefone,
            self.cnpjFornecedor,
        )

    def columns(self):
        return [
            '"endereco"',
            '"razao"',
            '"nome"',
            '"telefone"',
            '"cnpjFornecedor"',
        ]

    def auto_columns(self):
        return []

    def keys(self):
        return [
            '"cnpjFornecedor"',
        ]
