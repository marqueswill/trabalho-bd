class Lote:

    def __init__(self, numLote=None, tipo=None):
        self.numLote = numLote
        self.tipo = tipo

    def __str__(self):
        return "Lote"

    def to_tuple(self):
        return (self.tipo, self.numLote)

    def columns(self):
        return [
            '"tipo"',
            '"numLote"',
        ]
