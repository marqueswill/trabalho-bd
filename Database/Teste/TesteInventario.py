from TesteBase import TesteBase

from Integracao.DBInventario import DBInventario
from Objetos.Inventario import Inventario

class TesteInventario(TesteBase):
    def __init__(self):
        self.inventario_db = DBInventario(teste=True)

    def test_insert(self):
        try:
            inventarios = [
                Inventario(
                    codProduto="0001",
                    codEstoque="0001",
                    dataInv="2024-08-11",
                    contagem= 2068,
                    diferenca=0,
                    ajustado=False,
                    cpfEstoquista="12345678900"

                ),
                Inventario(
                    codProduto="0002",
                    codEstoque="0002",
                    dataInv="2024-09-03",
                    contagem=1906,
                    diferenca=0,
                    ajustado=False,
                    cpfEstoquista="12345678900"

                ),
                Inventario(
                    codProduto="0003",
                    codEstoque="0001",
                    dataInv="2024-08-11",
                    contagem=2068,
                    diferenca=0,
                    ajustado=False,
                    cpfEstoquista="12345678900"

                )
            ]
            for i in inventarios:
                self.inventario_db.insert(i)
            return "Sucess"
        except Exception as e:
            return f"Failed - {str(e)}"
    def test_get_by_id(self):
        try:
            inventario = self.inventario_db.get_by_id("0001")
            if inventario:
                return "Success"
            else:
                return "Failed - No fornecedor found"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_get_all(self):
        try:
            self.inventario_db.get_all()
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_delete(self):
        try:
            self.inventario_db.delete("0001")
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_delete_all(self):
        try:
            self.inventario_db.delete_all()
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"