from Teste.TesteBase import TesteBase
from Integracao.DBLote import DBLote
from Objetos.Lote import Lote


class TesteLote(TesteBase):
    def __init__(self):
        self.lote_db = DBLote(teste=True)

    def test_insert(self):
        try:
            lotes = [
                Lote(numLote=6, tipo="entrada"),
                Lote(numLote=7, tipo="ajuste"),
                Lote(numLote=8, tipo="requisicao"),
                Lote(numLote=9, tipo="saida"),
            ]
            for l in lotes:
                self.lote_db.insert(l)
            return "test_insert: Success"
        except Exception as e:
            return f"test_insert: Failed - {str(e)}"

    def test_get_by_id(self):
        try:
            lote = self.lote_db.get_by_id(6)
            if lote:
                return "test_get_by_id: Success"
            else:
                return "test_get_by_id: Failed - No lote found"
        except Exception as e:
            return f"test_get_by_id: Failed - {str(e)}"

    def test_get_all(self):
        try:
            self.lote_db.get_all()
            return "test_get_all: Success"
        except Exception as e:
            return f"test_get_all: Failed - {str(e)}"

    def test_delete(self):
        try:
            self.lote_db.delete(6)
            return "test_delete: Success"
        except Exception as e:
            return f"test_delete: Failed - {str(e)}"

    def test_delete_all(self):
        try:
            all_lotes = self.lote_db.delete_all()
            return "delete_all: Success"
        except Exception as e:
            return f"delete_all: Failed - {str(e)}"
