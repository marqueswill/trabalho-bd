from Database.Teste.TesteBase import TesteBase

from Database.Integracao.DBEntrada import DBEntrada
from Database.Objetos.Entrada import Entrada


class TesteEntrada(TesteBase):
    def __init__(self):
        self.entrada_db = DBEntrada(teste=True)

    def test_insert(self):
        try:
            items = [
                Entrada(
                    descricao="Entrada sucos",
                    dataLancamento="2024-08-01",
                    pendente=False,
                    aprovado=True,
                    numLote=6,
                    cpfEstoquista="45678901234",
                    cpfOperador="23456789012",
                    codEstoque=1,
                ),
                Entrada(
                    descricao="Entrada carnes",
                    dataLancamento="2024-08-05",
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
            entrada = self.entrada_db.get_by_id(11)
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
            entrada = self.entrada_db.get_by_id(12)
            entrada.descricao = "Entrada de varias coisas e tal"
            entrada.pendente = False
            entrada.aprovado = False
            self.entrada_db.update(entrada=self.entrada_db.get_by_id(12))
            return "Success"

        except Exception as e:
            return f"Failed - {str(e)}"

    def test_delete(self):
        try:
            e = self.entrada_db.delete(11)
            self.entrada_db.delete(e)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
