from Teste.TesteBase import TesteBase

from Integracao.DBEntrada import DBEntrada
from Objetos.Entrada import Entrada


class TesteEntrada(TesteBase):
    def __init__(self):
        self.entrada_db = DBEntrada(teste=True)

    def test_insert(self):
        try:
            items = [
                Entrada(
                    codOperacao=21,
                    descricao="Entrada sucos",
                    dataLancamento="2024-08-01",
                    dataConfirmacao="2024-08-02",
                    status="Confirmado",
                    pendente=False,
                    aprovado=True,
                    numLote=1,
                    cpfEstoquista="45678901234",
                    cpfOperador="23456789012"
                ),
                Entrada(
                    codOperacao=22,
                    descricao="Entrada carnes",
                    dataLancamento="2024-08-05",
                    dataConfirmacao="2024-08-06",
                    status="Pendente",
                    pendente=True,
                    aprovado=False,
                    numLote=2,
                    cpfEstoquista="45678901234",
                    cpfOperador="23456789012"
                ),
            ]
            for i in items:
                self.entrada_db.insert(i)
            return "test_insert: Success"
        except Exception as e:
            return f"test_insert: Failed - {str(e)}"

    def test_get_by_id(self):
        try:
            entrada = self.entrada_db.get_by_id(21)
            if entrada:
                return "test_get_by_id: Success"
            else:
                return "test_get_by_id: Failed - No entrada found"
        except Exception as e:
            return f"test_get_by_id: Failed - {str(e)}"

    def test_get_all(self):
        try:
            self.entrada_db.get_all()
            return "test_get_all: Success"
        except Exception as e:
            return f"test_get_all: Failed - {str(e)}"

    def test_delete(self):
        try:
            self.entrada_db.delete(21)
            return "test_delete: Success"
        except Exception as e:
            return f"test_delete: Failed - {str(e)}"

    def delete_all(self):
        try:
            self.entrada_db.delete_all()
            return "delete_all: Success"
        except Exception as e:
            return f"delete_all: Failed - {str(e)}"
