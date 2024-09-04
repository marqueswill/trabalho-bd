class Restaurante:
    def __init__(
        self,
        endereco,
        razao,
        nome,
        telefone,
        cnpjMatriz,
        cpfGerente,
        cnpjRestaurante,
    ):
        self.endereco = endereco
        self.razao = razao
        self.nome = nome
        self.telefone = telefone
        self.cnpjMatriz = cnpjMatriz
        self.cpfGerente = cpfGerente
        self.cnpjRestaurante = cnpjRestaurante

    def to_tuple(self):
        return (
            self.endereco,
            self.razao,
            self.nome,
            self.telefone,
            self.cnpjMatriz,
            self.cpfGerente,
            self.cnpjRestaurante,
        )
    
    def columns(self):
        return [
            '"endereco"',
            '"razao"',
            '"nome"',
            '"telefone"',
            '"cnpjMatriz"',
            '"cpfGerente"',
            '"cnpjRestaurante"',
        ]

