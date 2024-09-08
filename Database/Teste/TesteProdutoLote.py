from Database.Objetos.Lote import Lote
from Database.Teste.TesteBase import TesteBase
from Database.Integracao.DBProdutoLote import DBProdutoLote
from Database.Integracao.DBLote import DBLote

from Database.Objetos.ProdutoLote import ProdutoLote


class TesteProdutoLote(TesteBase):
    def __init__(self):
        self.produtolote_db = DBProdutoLote(teste=True)

    def test_insert(self):
        
        try:
            items = [
                ProdutoLote(codProduto=1, codEstoque=2, numLote=10, quantidade=10),
                ProdutoLote(codProduto=2, codEstoque=2, numLote=10, quantidade=20),
                ProdutoLote(codProduto=3, codEstoque=2, numLote=10, quantidade=30),
                ProdutoLote(codProduto=4, codEstoque=2, numLote=10, quantidade=40),
                ProdutoLote(codProduto=5, codEstoque=2, numLote=10, quantidade=50),
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
            p = self.produtolote_db.get_by_id(1, 1, 6)
            self.produtolote_db.delete(p)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
