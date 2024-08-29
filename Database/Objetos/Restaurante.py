class Restaurante:
    def __init__(
        self,
        cnpjRestaurante,
        endereco,
        razao,
        nome,
        telefone,
        cnpjMatriz,
        cpfGerente,
    ):
        self.cnpjRestaurante = cnpjRestaurante
        self.endereco = endereco
        self.razao = razao
        self.nome = nome
        self.telefone = telefone
        self.cnpjMatriz = cnpjMatriz
        self.cpfGerente = cpfGerente

    def to_tuple(self):
        return (
            self.cnpjRestaurante,
            self.endereco,
            self.razao,
            self.nome,
            self.telefone,
            self.cnpjMatriz,
            self.cpfGerente,
        )
