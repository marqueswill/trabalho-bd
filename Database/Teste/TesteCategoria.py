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
            print("test_insert: Success")
        except Exception as e:
            print(f"test_insert: Failed - {str(e)}")

    def test_get_by_id(self):
        try:
            categoria = self.categoria_db.get_by_id(1)
            if categoria:
                print("test_get_by_id: Success")
            else:
                print("test_get_by_id: Failed - No category found")
        except Exception as e:
            print(f"test_get_by_id: Failed - {str(e)}")

    def test_get_all(self):
        try:
            select_all = self.categoria_db.get_all()
            # for categoria in select_all:
            #     print(f"ID: {categoria.codCategoria}, Nome: {categoria.nome}")
            print("test_get_all: Success")
        except Exception as e:
            print(f"test_get_all: Failed - {str(e)}")

    def test_delete(self):
        try:
            self.categoria_db.delete(1)
            print("test_delete: Success")
        except Exception as e:
            print(f"test_delete: Failed - {str(e)}")

    def delete_all(self):
        try:
            all_categorias = self.categoria_db.get_all()
            for categoria in all_categorias:
                self.categoria_db.delete(categoria.codCategoria)
            print("delete_all: Success")
        except Exception as e:
            print(f"delete_all: Failed - {str(e)}")
