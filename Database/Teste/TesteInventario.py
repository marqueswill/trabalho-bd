from Database.Teste.TesteBase import TesteBase

from Database.Integracao.DBInventario import DBInventario
from Database.Objetos.Inventario import Inventario


class TesteInventario(TesteBase):
    def __init__(self):
        self.inventario_db = DBInventario(teste=True)

    def test_insert(self):
        try:
            inventarios = [
                Inventario(
                    codProduto=1,
                    codEstoque=1,
                    data="2024-08-11",
                    contagem=2068,
                    diferenca=0,
                    ajustado=False,
                    cpfEstoquista="12345678901",
                ),
                Inventario(
                    codProduto=2,
                    codEstoque=1,
                    data="2024-09-03",
                    contagem=1906,
                    diferenca=0,
                    ajustado=False,
                    cpfEstoquista="12345678901",
                ),
                Inventario(
                    codProduto=3,
                    codEstoque=1,
                    data="2024-08-11",
                    contagem=2068,
                    diferenca=0,
                    ajustado=False,
                    cpfEstoquista="12345678901",
                ),
            ]
            for i in inventarios:
                self.inventario_db.insert(i)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_get_by_id(self):
        try:
            inventario = self.inventario_db.get_by_id(2, 1, "2024-08-02")
            if inventario:
                return "Success"
            else:
                return "Failed - No fornecedor found"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_update(self):
        try:
            inv = self.inventario_db.get_by_id(
                codProduto=3,
                codEstoque=1,
                data="2024-08-11",
            )
            inv.contagem = 1000
            self.inventario_db.update(inv)

            return "Success"

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
            self.inventario_db.delete(1, 1, "2024-08-01")
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
