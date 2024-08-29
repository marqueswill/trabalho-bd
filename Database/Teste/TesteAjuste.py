from Teste.TesteLote import TesteLote
from Teste.TesteBase import TesteBase
from Integracao.DBAjuste import DBAjuste
from Objetos.Ajuste import Ajuste


class TesteAjuste(TesteBase):
    def __init__(self):
        super().__init__()

        self.ajuste_db = DBAjuste()
        self.setup_relations()

    def setup_relations(self):
        teste_ajuste = TesteLote()
        teste_ajuste.test_insert()
        # teste_funcionario = TesteFuncionario()
        # teste_funcionario.test_insert()
        # teste_inventario = TesteInventario()
        # teste_inventario.test_insert()

    def test_insert(self):
        try:

            ajustes = [
                Ajuste(
                    codOperacao=1,
                    descricao="Ajuste positivo",
                    dataLancamento="2024-08-01",
                    dataConfirmacao="2024-08-02",
                    status="Confirmado",
                    pendente=False,
                    aprovado=True,
                    numLote=1,
                    cpfEstoquista="12345678901",
                    cpfOperador="10987654321",
                    codProduto=1,
                    codEstoque=1,
                    dataInv="2024-08-01",
                ),
                Ajuste(
                    codOperacao=2,
                    descricao="Ajuste adicional",
                    dataLancamento="2024-08-05",
                    dataConfirmacao="2024-08-06",
                    status="Pendente",
                    pendente=True,
                    aprovado=False,
                    numLote=2,
                    cpfEstoquista="12345678901",
                    cpfOperador="10987654321",
                    codProduto=1,
                    codEstoque=1,
                    dataInv="2024-08-05",
                ),
            ]
            for a in ajustes:
                self.ajuste_db.insert(a)
            return "test_insert: Success"
        except Exception as e:
            return f"test_insert: Failed - {str(e)}"

    def test_get_by_id(self):
        try:
            ajuste = self.ajuste_db.get_by_id(1)
            if ajuste:
                return "test_get_by_id: Success"
            else:
                return "test_get_by_id: Failed - No ajuste found"
        except Exception as e:
            return f"test_get_by_id: Failed - {str(e)}"

    def test_get_all(self):
        try:
            self.ajuste_db.get_all()
            return "test_get_all: Success"
        except Exception as e:
            return f"test_get_all: Failed - {str(e)}"

    def test_delete(self):
        try:
            self.ajuste_db.delete(1)
            return "test_delete: Success"
        except Exception as e:
            return f"test_delete: Failed - {str(e)}"

    def delete_all(self):
        try:
            self.ajuste_db.delete_all()
            return "delete_all: Success"
        except Exception as e:
            return f"delete_all: Failed - {str(e)}"
