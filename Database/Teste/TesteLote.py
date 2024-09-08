from Database.Teste.TesteBase import TesteBase
from Database.Integracao.DBLote import DBLote
from Database.Objetos.Lote import Lote


class TesteLote(TesteBase):
    def __init__(self):
        self.lote_db = DBLote(teste=True)

    def test_insert(self):
        try:
            lotes = [
                Lote(tipo="entrada"),
                Lote(tipo="entrada"),
                Lote(tipo="saida"),
                Lote(tipo="saida"),
            ]
            for l in lotes:
                self.lote_db.insert(l)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_get_by_id(self):
        try:
            lote = self.lote_db.get_by_id(11)
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
            lote = self.lote_db.get_by_id(12)
            lote.tipo = "entrada"
            self.lote_db.update(lote)
            return "Success"

        except Exception as e:
            return f"Failed - {str(e)}"

    def test_delete(self):
        try:
            l = self.lote_db.get_by_id(11)
            self.lote_db.delete(l)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
