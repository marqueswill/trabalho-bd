from Teste.TesteBase import TesteBase
from Integracao.DBLote import DBLote
from Objetos.Lote import Lote


class TesteLote(TesteBase):
    def __init__(self):
        super().__init__()
        self.lote_db = DBLote()

    def test_insert(self):
        try:
            lotes = [
                Lote(numLote=1, tipo="entrada"),
                Lote(numLote=2, tipo="ajuste"),
            ]
            for l in lotes:
                self.lote_db.insert(l)
            return "test_insert: Success"
        except Exception as e:
            return f"test_insert: Failed - {str(e)}"

    def test_get_by_id(self):
        try:
            lote = self.lote_db.get_by_id(1)
            if lote:
                return "test_get_by_id: Success"
            else:
                return "test_get_by_id: Failed - No lot found"
        except Exception as e:
            return f"test_get_by_id: Failed - {str(e)}"

    def test_get_all(self):
        try:
            select_all = self.lote_db.get_all()
            return "test_get_all: Success"
        except Exception as e:
            return f"test_get_all: Failed - {str(e)}"

    def test_delete(self):
        try:
            self.lote_db.delete(1)
            return "test_delete: Success"
        except Exception as e:
            return f"test_delete: Failed - {str(e)}"

    def delete_all(self):
        try:
            all_lotes = self.lote_db.get_all()
            for lote in all_lotes:
                self.lote_db.delete(lote.numLote)
            return "delete_all: Success"
        except Exception as e:
            return f"delete_all: Failed - {str(e)}"
