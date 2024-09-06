from Objetos.Lote import Lote
from Teste.TesteBase import TesteBase
from Integracao.DBProdutoLote import DBProdutoLote
from Integracao.DBLote import DBLote

from Objetos.ProdutoLote import ProdutoLote


class TesteProdutoLote(TesteBase):
    def __init__(self):
        self.produtolote_db = DBProdutoLote(teste=True)
        self.lote_db = DBLote(teste=True)        

    def test_insert(self):
        self.lote_db.insert(Lote("entrada"))
        try:
            items = [
                ProdutoLote(codProduto=1, codEstoque=1, numLote=11, quantidade=10),
                ProdutoLote(codProduto=2, codEstoque=1, numLote=11, quantidade=20),
                ProdutoLote(codProduto=3, codEstoque=1, numLote=11, quantidade=30),
                ProdutoLote(codProduto=4, codEstoque=1, numLote=11, quantidade=40),
                ProdutoLote(codProduto=5, codEstoque=1, numLote=11, quantidade=50),
            ]
            for i in items:
                self.produtolote_db.insert(i)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_get_by_id(self):
        try:
            produtolote = self.produtolote_db.get_by_id(1, 1, 6)
            if produtolote:
                return "Success"
            else:
                return "Failed - No produtolote found"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_get_all(self):
        try:
            self.produtolote_db.get_all()
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_update(self):
        try:
            produtolote = self.produtolote_db.get_by_id(2, 1, 6)
            produtolote.tipo = "entrada"
            self.produtolote_db.update(produtolote)
            return "Success"

        except Exception as e:
            return f"Failed - {str(e)}"

    def test_delete(self):
        try:
            self.produtolote_db.delete(1, 1, 6)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
