from Database.Teste.TesteBase import TesteBase
from Database.Integracao.DBProdutoEstoque import DBProdutoEstoque
from Database.Objetos.ProdutoEstoque import ProdutoEstoque

class TesteProdutoEstoque(TesteBase):
    def __init__(self):
        super().__init__()
        self.produtoEstoque_db = DBProdutoEstoque(teste=True)

    def test_insert(self):
        try:
            items = [
                ProdutoEstoque(codProduto=1, codEstoque=2, estoqueMax=100, estoqueMin=50, estoqueAtual=0, estoqueDisp=0, ultimoInv='2024-09-02'),
                ProdutoEstoque(codProduto=2, codEstoque=2, estoqueMax=500, estoqueMin=70, estoqueAtual=0, estoqueDisp=0, ultimoInv='2023-09-02'),
            ]
            for item in items:
                self.produtoEstoque_db.insert(item)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
        
    def test_get_by_id(self):
        try:
            produtoEstoque = self.produtoEstoque_db.get_by_id(1, 2)
            if produtoEstoque:
                return "Success"
            return "Failed - No ProdutoEstoque found"
        except Exception as e:
            return f"Failed - {str(e)}"
        
    def test_get_all(self):
        try:
            self.produtoEstoque_db.get_all()
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
        
    def test_update(self):
        try:
            produtoEstoque = self.produtoEstoque_db.get_by_id(1, 2)
            produtoEstoque.estoqueMax = 150
            self.produtoEstoque_db.update(produtoEstoque)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
        
    def test_delete(self):
        try:
            self.produtoEstoque_db.delete(2,2)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"