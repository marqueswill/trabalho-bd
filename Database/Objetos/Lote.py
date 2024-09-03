class Lote:
    def __init__(self, numLote=0, tipo=""):
        self.numLote = numLote
        self.tipo = tipo

    def to_tuple(self):
        return (self.tipo, self.numLote)

    def columns(self):
        return [
            '"tipo"',
            '"numLote"',
        ]
