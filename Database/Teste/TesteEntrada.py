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
                    numLote=6,
                    cpfEstoquista="45678901234",
                    cpfOperador="23456789012",
                    codEstoque=1,
                ),
                Entrada(
                    codOperacao=22,
                    descricao="Entrada carnes",
                    dataLancamento="2024-08-05",
                    dataConfirmacao="2024-08-06",
                    status="Pendente",
                    pendente=True,
                    aprovado=False,
                    numLote=7,
                    cpfEstoquista="45678901234",
                    cpfOperador="23456789012",
                    codEstoque=1,
                ),
            ]
            for i in items:
                self.entrada_db.insert(i)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_get_by_id(self):
        try:
            entrada = self.entrada_db.get_by_id(21)
            if entrada:
                return "Success"
            else:
                return "Failed - No entrada found"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_get_all(self):
        try:
            self.entrada_db.get_all()
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_update(self):
        try:
            entrada = self.entrada_db.get_by_id(22)
            entrada.descricao = "Entrada de varias coisas e tal"
            entrada.pendente = False
            entrada.aprovado = False
            self.entrada_db.update(entrada=self.entrada_db.get_by_id(22))
            return "Success"

        except Exception as e:
            return f"Failed - {str(e)}"

    def test_delete(self):
        try:
            self.entrada_db.delete(21)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"