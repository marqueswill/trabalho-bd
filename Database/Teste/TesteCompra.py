from base64 import decode
from Teste.TesteBase import TesteBase
from Integracao.DBCompra import DBCompra
from Objetos.Compra import Compra


class TesteCompra(TesteBase):
    def __init__(self):
        super().__init__()
        self.compra_db = DBCompra(teste=True)

    def test_insert(self):
        try:
            compras = [
                Compra(codOperacao=1, cnpjFornecedor='12345678000199', cnpjRestaurante='98765432000199', notaFiscal=decode('DEADBEEF', 'hex'), data='2024-09-02', quantidade=100),
                Compra(codOperacao=2, cnpjFornecedor='23456789000188', cnpjRestaurante='98765432000199', notaFiscal=decode('CAFEBABE', 'hex'), data='2024-09-02', quantidade=200),
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
            compra.quantidade = 1000
            self.compra_db.update(compra)
            return "Success"

        except Exception as e:
            return f"Failed - {str(e)}"

    def test_delete(self):
        try:
            self.compra_db.delete(1, '12345678000199', '98765432000199')
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def delete_all(self):
        try:
            self.compra_db.delete_all()
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
