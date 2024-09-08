class Lote:

    def __init__(
        self,
        tipo=None,
        numLote=None,
    ):
        self.tipo = tipo
        self.numLote = numLote

    def __str__(self):
        return "Lote"

    def to_tuple(self):
        return (
            self.tipo,
            self.numLote,
        )

    def columns(self):
        return [
            '"tipo"',
            '"numLote"',
        ]

    def auto_columns(self):
        return [
            '"numLote"',
        ]

    def keys(self):
        return [
            '"numLote"',
        ]
