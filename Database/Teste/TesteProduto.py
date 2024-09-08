from Database.Integracao.DBProduto import DBProduto
from Database.Objetos.Produto import Produto
from Database.Teste.TesteBase import TesteBase

class TesteProduto(TesteBase):
    def __init__(self):
        self.produto_db = DBProduto(teste=True)
    
    def test_insert(self):
        try:
            produtos = [
                Produto(
                    unidade="kg",
                    quantidade=75,
                    nome="Picanha",
                    descricao="Picanha embalada a vacuo",
                    codCategoria=1,
                    codProduto=51,
                ),
                Produto(
                    unidade="g",
                    quantidade=206,
                    nome="Baccio",
                    descricao="Sorvete de Pistache",
                    codCategoria=7,
                    codProduto=52,
                )
            ]
            for f in produtos:
                self.produto_db.insert(f)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
    
    def test_get_by_id(self):
        try:
            produto = self.produto_db.get_by_id(51)

            if produto:
                return "Success"
            else:
                return "Failed - No produto found"
        except Exception as e:
            return f"Failed - {str(e)}"
    
    def test_get_all(self):
        try:
            self.produto_db.get_all()
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
        
    
    def test_update(self):
        try:
            produto = self.produto_db.get_by_id(51)
            produto.quantidade = 52
            produto.descricao = "Suco de laranja natural"
            produto.nome = "JuiceOrange"
            self.produto_db.update(produto)

            return "Success"

        except Exception as e:
            return f"Failed - {str(e)}"
        
    def test_delete(self):
        try:
            f = self.produto_db.get_by_id(52)
            self.produto_db.delete(f)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"