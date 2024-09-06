class Categoria:

    def __init__(self, codCategoria=None, nome=None):
        self.codCategoria = codCategoria
        self.nome = nome

    def __str__(self):
        return "Categoria"

    def to_tuple(self):
        return (
            self.codCategoria,
            self.nome,
        )

    def columns(self):
        return [
            '"codCategoria"',
            '"nome"',
        ]
