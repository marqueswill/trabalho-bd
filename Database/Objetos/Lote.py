class Lote:
    def __init__(self, numLote, tipo):
        self.numLote = numLote
        self.tipo = tipo

    def to_tuple(self):
        return (self.numLote, self.tipo)
