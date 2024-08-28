class Categoria:
    def __init__(self, idCategoria, nome):
        self.idCategoria = idCategoria
        self.nome = nome

    def to_tuple(self):
        return (self.idCategoria, self.nome)