from Teste.TesteLote import TesteLote
from Teste.TesteBase import TesteBase
from Teste.TesteFuncionario import TesteFuncionario

from Integracao.DBSaida import DBSaida
from Integracao.DBRequisicao import DBRequisicao

from Objetos.Saida import Saida


class TesteSaida(TesteBase):
    def __init__(self):
        self.saida_db = DBSaida(teste=True)
        # self.requisicao_db = DBRequisicao(teste=True)

    def test_insert(self):
        try:
            items = [
                Saida(
                    # codOperacao=21,
                    descricao="Saida sucos",
                    dataLancamento="2024-08-01",
                    # dataConfirmacao=None,
                    # status="Confirmado",
                    pendente=True,
                    aprovado=False,
                    numLote=1,
                    cpfEstoquista="45678901234",
                    cpfOperador="23456789012",
                    codEstoque=1,
                    # codRequisicao=6,
                ),
                Saida(
                    # codOperacao=22,
                    descricao="Saida carnes",
                    dataLancamento="2024-08-05",
                    dataConfirmacao=None,
                    # status="Pendente",
                    pendente=True,
                    aprovado=False,
                    numLote=2,
                    cpfEstoquista="45678901234",
                    cpfOperador="23456789012",
                    codEstoque=1,
                    # codRequisicao=7,
                ),
            ]
            for i in items:
                self.saida_db.insert(i)

            self.saida_db.get_by_id(1)
            self.saida_db.get_by_id(2)

            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_get_by_id(self):
        try:
            saida = self.saida_db.get_by_id(1)
            if saida:
                return "Success"
            else:
                return "Failed - No saida found"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_get_all(self):
        try:
            self.saida_db.get_all()
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_delete(self):
        try:
            self.saida_db.delete(1)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_update(self):
        try:
            saida = self.saida_db.get_by_id(2)
            saida.descricao = "Saida de varias coisas e tal"

            self.saida_db.update(saida)
            return "Success"

        except Exception as e:
            return f"Failed - {str(e)}"

    def test_delete_all(self):
        try:
            self.saida_db.delete_all()
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
