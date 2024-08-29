from Teste.TesteBase import TesteBase
from Integracao.DBCategoria import DBCategoria
from Objetos.Categoria import Categoria


class TesteCategoria(TesteBase):
    def __init__(self):
        super().__init__()
        self.categoria_db = DBCategoria()

    def test_insert(self):
        try:
            categorias = [
                Categoria(codCategoria=1, nome="sucos"),
                Categoria(codCategoria=2, nome="carnes"),
            ]
            for c in categorias:
                self.categoria_db.insert(c)
            return("test_insert: Success")
        except Exception as e:
            return(f"test_insert: Failed - {str(e)}")

    def test_get_by_id(self):
        try:
            categoria = self.categoria_db.get_by_id(1)
            if categoria:
                return("test_get_by_id: Success")
            else:
                return("test_get_by_id: Failed - No category found")
        except Exception as e:
            return(f"test_get_by_id: Failed - {str(e)}")

    def test_get_all(self):
        try:
            select_all = self.categoria_db.get_all()
            # for categoria in select_all:
            #     return(f"ID: {categoria.codCategoria}, Nome: {categoria.nome}")
            return("test_get_all: Success")
        except Exception as e:
            return(f"test_get_all: Failed - {str(e)}")

    def test_delete(self):
        try:
            self.categoria_db.delete(1)
            return("test_delete: Success")
        except Exception as e:
            return(f"test_delete: Failed - {str(e)}")

    def delete_all(self):
        try:
            all_categorias = self.categoria_db.get_all()
            for categoria in all_categorias:
                self.categoria_db.delete(categoria.codCategoria)
            return("delete_all: Success")
        except Exception as e:
            return(f"delete_all: Failed - {str(e)}")
