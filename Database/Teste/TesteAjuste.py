from Teste.TesteLote import TesteLote
from Teste.TesteBase import TesteBase
from Integracao.DBAjuste import DBAjuste
from Objetos.Ajuste import Ajuste


class TesteAjuste(TesteBase):
    def __init__(self):
        super().__init__()
        self.ajuste_db = DBAjuste(teste=True)

    def test_insert(self):
        try:

            ajustes = [
                Ajuste(
                    codOperacao=21,
                    descricao="Ajuste positivo",
                    dataLancamento="2024-08-01",
                    dataConfirmacao="2024-08-02",
                    status="Confirmado",
                    pendente=False,
                    aprovado=True,
                    numLote=1,
                    cpfEstoquista="45678901234",
                    cpfOperador="23456789012",
                    codProduto=1,
                    codEstoque=1,
                    dataInv="2024-08-01",
                ),
                Ajuste(
                    codOperacao=22,
                    descricao="Ajuste adicional",
                    dataLancamento="2024-08-05",
                    dataConfirmacao="2024-08-06",
                    status="Pendente",
                    pendente=True,
                    aprovado=False,
                    numLote=2,
                    cpfEstoquista="45678901234",
                    cpfOperador="23456789012",
                    codProduto=2,
                    codEstoque=1,
                    dataInv="2024-08-02",
                ),
            ]
            for a in ajustes:
                self.ajuste_db.insert(a)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_get_by_id(self):
        try:
            ajuste = self.ajuste_db.get_by_id(21)
            if ajuste:
                return "Success"
            else:
                return "Failed - No ajuste found"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_get_all(self):
        try:
            self.ajuste_db.get_all()
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_update(self):
        try:
            ajuste = self.ajuste_db.get_by_id(22)
            ajuste.descricao = "Ajuste de varias coisas e tal"
            ajuste.status = "recusado"
            ajuste.pendente = False
            ajuste.aprovado = False

            self.ajuste_db.update(ajuste)
            return "Success"

        except Exception as e:
            return f"Failed - {str(e)}"

    def test_delete(self):
        try:
            self.ajuste_db.delete(21)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def delete_all(self):
        try:
            self.ajuste_db.delete_all()
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
