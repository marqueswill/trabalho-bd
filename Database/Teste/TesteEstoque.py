from Database.Teste.TesteBase import TesteBase
from Database.Integracao.DBEstoque import DBEstoque
from Database.Objetos.Estoque import Estoque


class TesteEstoque(TesteBase):
    def __init__(self):
        super().__init__()
        self.estoque_db = DBEstoque(teste=True)

    def test_insert(self):
        try:
            estoques = [
                Estoque(
                    nome="Estoque 1", cnpjRestaurante="98765432000199"
                ),
                Estoque(
                    nome="Estoque 2", cnpjRestaurante="98765432000199"
                ),
            ]
            for estoque in estoques:
                self.estoque_db.insert(estoque)
            return "Success"
        except Exception as e:
            f"Failed - {str(e)}"

    def test_update(self):
        try:
            estoque = self.estoque_db.get_by_id(6)
            estoque.nome = "Estoque Update"
            self.estoque_db.update(estoque)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_get_by_id(self):
        try:
            estoque = self.estoque_db.get_by_id(6)
            if estoque:
                return "Success"
            else:
                return "Failed - No Estoque found"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_get_all(self):
        try:
            self.estoque_db.get_all()
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_delete(self):
        try:
            e = self.estoque_db.get_by_id(6)
            self.estoque_db.delete(e)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
