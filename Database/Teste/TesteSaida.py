from Teste.TesteLote import TesteLote
from Teste.TesteBase import TesteBase
from Teste.TesteFuncionario import TesteFuncionario

from Integracao.DBSaida import DBSaida
from Integracao.DBLote import DBLote
from Integracao.DBProdutoLote import DBProdutoLote

from Objetos.Saida import Saida
from Objetos.Lote import Lote
from Objetos.ProdutoLote import ProdutoLote


class TesteSaida(TesteBase):
    def __init__(self):
        self.saida_db = DBSaida(teste=True)
        self.lote_db = DBLote(teste=True)
        self.produtolote_db = DBProdutoLote(teste=True)

    def test_insert(self):
        try:
            self.lote_db.insert(Lote(tipo="saida"))
            self.produtolote_db.insert(ProdutoLote(1,1,11,10))
            
            items = [
                Saida(
                    descricao="Saida sucos",
                    dataLancamento="2024-08-01",
                    pendente=True,
                    aprovado=False,
                    numLote=1,
                    cpfEstoquista="45678901234",
                    cpfOperador="23456789012",
                    codEstoque=1,
                ),
                Saida(
                    descricao="Saida carnes",
                    dataLancamento="2024-08-05",
                    dataConfirmacao=None,
                    pendente=True,
                    aprovado=False,
                    numLote=2,
                    cpfEstoquista="45678901234",
                    cpfOperador="23456789012",
                    codEstoque=1,
                ),
            ]
            for i in items:
                self.saida_db.insert(i)

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


