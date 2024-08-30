from Teste.TesteBase import TesteBase

from Integracao.DBRequisicao import DBRequisicao
from Objetos.Requisicao import Requisicao


class TesteRequisicao(TesteBase):
    def __init__(self):
        self.requisicao_db = DBRequisicao(teste=True)

    def test_insert(self):
        try:
            items = [
                Requisicao(
                    codOperacao=21,
                    descricao="Requisicao sucos",
                    dataLancamento="2024-08-01",
                    dataConfirmacao="2024-08-02",
                    status="aprovado",
                    pendente=False,
                    aprovado=True,
                    numLote=1,
                    cpfEstoquista="45678901234",
                    cpfOperador="23456789012",
                ),
                Requisicao(
                    codOperacao=22,
                    descricao="Requisicao carnes",
                    dataLancamento="2024-08-05",
                    dataConfirmacao=None,
                    status="pendente",
                    pendente=True,
                    aprovado=False,
                    numLote=2,
                    cpfEstoquista="45678901234",
                    cpfOperador="23456789012",
                ),
            ]
            for i in items:
                self.requisicao_db.insert(i)
            return "test_insert: Success"
        except Exception as e:
            return f"test_insert: Failed - {str(e)}"

    def test_get_by_id(self):
        try:
            requisicao = self.requisicao_db.get_by_id(22)
            if requisicao:
                return "test_get_by_id: Success"
            else:
                return "test_get_by_id: Failed - No requisicao found"
        except Exception as e:
            return f"test_get_by_id: Failed - {str(e)}"

    def test_get_all(self):
        try:
            self.requisicao_db.get_all()
            return "test_get_all: Success"
        except Exception as e:
            return f"test_get_all: Failed - {str(e)}"

    def test_update(self):
        try:
            requisicao = self.requisicao_db.get_by_id(22)
            requisicao.status = "recusado"
            requisicao.pendente = False
            requisicao.aprovado = False

            self.requisicao_db.update(requisicao)
            return "test_update: Success"
        except Exception as e:
            return f"test_update: Failed - {str(e)}"

    def test_delete(self):
        try:
            self.requisicao_db.delete(21)
            return "test_delete: Success"
        except Exception as e:
            return f"test_delete: Failed - {str(e)}"

    def delete_all(self):
        try:
            self.requisicao_db.delete_all()
            return "delete_all: Success"
        except Exception as e:
            return f"delete_all: Failed - {str(e)}"
