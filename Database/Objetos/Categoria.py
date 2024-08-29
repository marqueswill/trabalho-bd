class Categoria:
    def __init__(self, codCategoria, nome):
        self.codCategoria = codCategoria
        self.nome = nome

    def to_tuple(self):
        return (self.codCategoria, self.nome)
