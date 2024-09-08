from Database.Teste.TesteBase import TesteBase
from Database.Integracao.DBCompra import DBCompra
from Database.Objetos.Compra import Compra


class TesteCompra(TesteBase):
    def __init__(self):
        super().__init__()
        self.compra_db = DBCompra(teste=True)

    def test_insert(self):
        try:
            pdf_1 = self.compra_db.get_as_bytea("./Input/nota-fiscal.pdf")

            compras = [
                Compra(
                    codOperacao=1,
                    cnpjFornecedor="12345678000199",
                    cnpjRestaurante="98765432000199",
                    notaFiscal=pdf_1,
                    data="2024-09-02",
                    numNF=1001,
                ),
                Compra(
                    codOperacao=2,
                    cnpjFornecedor="23456789000188",
                    cnpjRestaurante="98765432000199",
                    notaFiscal=pdf_1,
                    data="2024-09-02",
                    numNF=1002,
                ),
            ]

            for c in compras:
                self.compra_db.insert(c)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_get_by_id(self):
        try:
            compra = self.compra_db.get_by_id(1001)
            if compra:
                compra.export_pdf("./Output/")
                return "Success"
            else:
                return "Failed - No compra found"
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
            compra = self.compra_db.get_by_id(1002)
            compra.data = "2023-09-02"
            self.compra_db.update(compra)
            return "Success"

        except Exception as e:
            return f"Failed - {str(e)}"

    def test_delete(self):
        try:
            c = self.compra_db.get_by_id(1001)
            self.compra_db.delete(c)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
