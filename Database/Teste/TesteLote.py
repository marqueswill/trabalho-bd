from Teste.TesteBase import TesteBase
from Integracao.DBLote import DBLote
from Objetos.Lote import Lote


class TesteLote(TesteBase):
    def __init__(self):
        self.lote_db = DBLote(teste=True)

    def test_insert(self):
        try:
            lotes = [
                Lote(numLote=21, tipo="entrada"),
                Lote(numLote=22, tipo="ajuste"),
                Lote(numLote=23, tipo="requisicao"),
                Lote(numLote=24, tipo="saida"),
            ]
            for l in lotes:
                self.lote_db.insert(l)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_get_by_id(self):
        try:
            lote = self.lote_db.get_by_id(21)
            if lote:
                return "Success"
            else:
                return "Failed - No lote found"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_get_all(self):
        try:
            self.lote_db.get_all()
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_update(self):
        try:
            lote = self.lote_db.get_by_id(22)
            lote.tipo = "entrada"
            self.lote_db.update(lote)
            return "Success"

        except Exception as e:
            return f"Failed - {str(e)}"

    def test_delete(self):
        try:
            self.lote_db.delete(21)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_delete_all(self):
        try:
            self.lote_db.delete_all()
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
