class Fornecedor:
    def __init__(self, cnpjFornecedor, endereco, razao, nome, telefone=None):
        self.endereco = endereco
        self.razao = razao
        self.nome = nome
        self.telefone = telefone
        self.cnpjFornecedor = cnpjFornecedor

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
