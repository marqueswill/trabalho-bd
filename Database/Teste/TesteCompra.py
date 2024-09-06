from reportlab.pdfgen import canvas
import os

from Teste.TesteBase import TesteBase
from Integracao.DBCompra import DBCompra
from Objetos.Compra import Compra


class TesteCompra(TesteBase):
    def __init__(self):
        super().__init__()
        self.compra_db = DBCompra(teste=True)

    def ler_pdf_como_bytea(self, pdf_path):
        """Lê um arquivo PDF e o converte para binário"""
        try:
            with open(pdf_path, 'rb') as file:
                return file.read()
        except Exception as e:
            print(f"Erro ao ler o arquivo PDF: {e}")
            return None

    def test_insert(self):
        try:
            pdf_1 = self.ler_pdf_como_bytea("nota-fiscal.pdf")
            # pdf_2 = self.ler_pdf_como_bytea(pdf_path_2)

            compras = [
                Compra(codOperacao=1, cnpjFornecedor='12345678000199', cnpjRestaurante='98765432000199', notaFiscal=pdf_1, data='2024-09-02'),
                Compra(codOperacao=2, cnpjFornecedor='23456789000188', cnpjRestaurante='98765432000199', notaFiscal=pdf_1, data='2024-09-02'),
            ]

            for c in compras:
                self.compra_db.insert(c)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_get_by_id(self):
        try:
            compra = self.compra_db.get_by_id(1, '12345678000199', '98765432000199')
            if compra:
                 
                compra.export_pdf(".")
                return "Success"
            else:
                return "Failed - No category found"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_get_all(self):
        try:
            self.compra_db.get_all()
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_update(self):
        try:
            compra = self.compra_db.get_by_id(2, '23456789000188', '98765432000199')
            compra.data = '2023-09-02'
            self.compra_db.update(compra)
            return "Success"

        except Exception as e:
            return f"Failed - {str(e)}" 

    def test_delete(self):
        try:
            self.compra_db.delete(1, "12345678000199", "98765432000199")
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def delete_all(self):
        try:
            self.compra_db.delete_all()
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
