from Database.Teste.TesteBase import TesteBase
from Database.Integracao.DBCategoria import DBCategoria
from Database.Objetos.Categoria import Categoria


class TesteCategoria(TesteBase):
    def __init__(self):
        super().__init__()
        self.categoria_db = DBCategoria(teste=True)

    def test_insert(self):
        try:
            categorias = [
                Categoria(nome="sucos"),
                Categoria(nome="carnes"),
            ]
            for c in categorias:
                self.categoria_db.insert(c)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_get_by_id(self):
        try:
            categoria = self.categoria_db.get_by_id(1)
            if categoria:
                return "Success"
            else:
                return "Failed - No category found"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_get_all(self):
        try:
            select_all = self.categoria_db.get_all()
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_update(self):
        try:
            cat = self.categoria_db.get_by_id(11)
            cat.nome = "Pratos e panelas"
            self.categoria_db.update(cat)
            return "Success"

        except Exception as e:
            return f"Failed - {str(e)}"

    def test_delete(self):
        try:
            c = self.categoria_db.get_by_id(11)
            self.categoria_db.delete(c)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
