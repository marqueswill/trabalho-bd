from reportlab.pdfgen import canvas
import os

class Compra:
    def __init__(self, codOperacao, cnpjFornecedor, cnpjRestaurante, notaFiscal, data):
        self.codOperacao = codOperacao
        self.cnpjFornecedor = cnpjFornecedor
        self.cnpjRestaurante = cnpjRestaurante
        self.notaFiscal = notaFiscal
        self.data = data
        #self.quantidade = quantidade

    def to_tuple(self):
        return (
            self.data,
            self.notaFiscal,
            self.codOperacao,
            self.cnpjFornecedor,
            self.cnpjRestaurante,
            #self.quantidade
        )
    
    def export_pdf(self, destino, remove=False):
        source = destino + self.numNF + "_" + self.data + ".pdf"
        c = canvas.Canvas(source)
        c.showPage()
        c.save()

        with open(source, 'wb') as output_file:
            output_file.write(self.notaFiscal)
            if remove:
                os.remove(source)
