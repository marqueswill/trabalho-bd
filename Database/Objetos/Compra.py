from reportlab.pdfgen import canvas
import os


class Compra:

    def __init__(
        self,
        codOperacao=None,
        cnpjFornecedor=None,
        cnpjRestaurante=None,
        notaFiscal=None,
        data=None,
        numNF=None,
    ):
        self.codOperacao = codOperacao
        self.cnpjFornecedor = cnpjFornecedor
        self.cnpjRestaurante = cnpjRestaurante
        self.notaFiscal = notaFiscal
        self.data = data
        self.numNF = numNF

    def __str__(self):
        return "Compra"

    def to_tuple(self):
        return (
            self.codOperacao,
            self.cnpjFornecedor,
            self.cnpjRestaurante,
            self.notaFiscal,
            self.data,
            self.numNF,
        )

    def export_pdf(self, destino="./Output/", remove=False):
        source = destino + str(self.numNF) + "_" + str(self.data) + ".pdf"
        c = canvas.Canvas(source)
        c.showPage()
        c.save()

        with open(source, "wb") as output_file:
            output_file.write(self.notaFiscal)
            if remove:
                os.remove(source)

    def columns(self):
        return [
            '"codOperacao"',
            '"cnpjFornecedor"',
            '"cnpjRestaurante"',
            '"notaFiscal"',
            '"data"',
            '"numNF"',
        ]

    def auto_columns(self):
        return []

    def keys(self):
        return [
            '"numNF"',
        ]
