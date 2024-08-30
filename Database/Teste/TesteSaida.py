from Teste.TesteLote import TesteLote
from Teste.TesteBase import TesteBase
from Teste.TesteFuncionario import TesteFuncionario

from Integracao.DBSaida import DBSaida
from Objetos.Saida import Saida


class TesteSaida(TesteBase):
    def __init__(self):
        self.saida_db = DBSaida(teste=True)
        
    def test_insert(self):
        try:
            self.setup_relations()
            saidas = [
                Saida(
                    codOperacao=1,
                    descricao="Saida sucos",
                    dataLancamento="2024-08-01",
                    dataConfirmacao="2024-08-02",
                    status="Confirmado",
                    pendente=False,
                    aprovado=True,
                    numLote=1,
                    cpfEstoquista="12345678999",
                    cpfOperador="09876543211",
                    codRequisicao=3,
                ),
                Saida(
                    codOperacao=2,
                    descricao="Saida carnes",
                    dataLancamento="2024-08-05",
                    dataConfirmacao="2024-08-06",
                    status="Pendente",
                    pendente=True,
                    aprovado=False,
                    numLote=2,
                    cpfEstoquista="12345678999",
                    cpfOperador="09876543211",
                    codRequisicao=3,
                ),
            ]
            for s in saidas:
                self.saida_db.insert(s)
            return "test_insert: Success"
        except Exception as e:
            return f"test_insert: Failed - {str(e)}"

    def test_get_by_id(self):
        try:
            saida = self.saida_db.get_by_id(1)
            if saida:
                return "test_get_by_id: Success"
            else:
                return "test_get_by_id: Failed - No saida found"
        except Exception as e:
            return f"test_get_by_id: Failed - {str(e)}"

    def test_get_all(self):
        try:
            self.saida_db.get_all()
            return "test_get_all: Success"
        except Exception as e:
            return f"test_get_all: Failed - {str(e)}"

    def test_delete(self):
        try:
            self.saida_db.delete(1)
            return "test_delete: Success"
        except Exception as e:
            return f"test_delete: Failed - {str(e)}"

    def delete_all(self):
        try:
            self.saida_db.delete_all()
            return "delete_all: Success"
        except Exception as e:
            return f"delete_all: Failed - {str(e)}"
