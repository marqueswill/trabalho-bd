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
                    descricao="Requisicao sucos",
                    dataLancamento="2024-08-01",
                    dataConfirmacao="2024-08-02",
                    status="aprovado",
                    pendente=True,
                    aprovado=False,
                    numLote=1,
                    cpfEstoquista="45678901234",
                    cpfOperador="23456789012",
                    codEstoque=1,
                ),
                Requisicao(
                    descricao="Requisicao carnes",
                    dataLancamento="2024-08-05",
                    dataConfirmacao=None,
                    status="pendente",
                    pendente=False,
                    aprovado=True,
                    numLote=2,
                    cpfEstoquista="45678901234",
                    cpfOperador="23456789012",
                    codEstoque=1,
                ),
            ]
            for i in items:
                self.requisicao_db.insert(i)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_get_by_id(self):
        try:
            requisicao = self.requisicao_db.get_by_id(7)
            if requisicao:
                return "Success"
            else:
                return "Failed - No requisicao found"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_get_all(self):
        try:
            self.requisicao_db.get_all()
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_update(self):
        try:
            requisicao = self.requisicao_db.get_by_id(7)
            requisicao.status = "recusado"
            requisicao.pendente = False
            requisicao.aprovado = False

            self.requisicao_db.update(requisicao)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_delete(self):
        try:
            self.requisicao_db.delete(6)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def delete_all(self):
        try:
            self.requisicao_db.delete_all()
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
