class Fornecedor:
    def __init__(self, cnpjFornecedor, endereco, razao, nome, telefone=None):
        self.cnpjFornecedor = cnpjFornecedor
        self.endereco = endereco
        self.razao = razao
        self.nome = nome
        self.telefone = telefone

    def to_tuple(self):
        return (
            self.cnpjFornecedor,
            self.endereco,
            self.razao,
            self.nome,
            self.telefone,
        )
