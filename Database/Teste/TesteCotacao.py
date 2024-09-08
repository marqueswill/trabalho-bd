from Database.Teste.TesteBase import TesteBase
from Database.Integracao.DBCotacao import DBCotacao
from Database.Objetos.Cotacao import Cotacao

class TesteCotacao(TesteBase):
    def __init__(self):
        super().__init__()
        self.cotacao_db = DBCotacao(teste=True)

    def test_insert(self):
        try:
            items = [Cotacao(valor=150.00, codProduto=10, cnpjFornecedor="12345678000199"),
                     Cotacao(valor=75.50, codProduto=9, cnpjFornecedor="12345678000199")]
            for item in items:
                self.cotacao_db.insert(item)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
        
    def test_get_by_id(self):
        try:
            cotacao = self.cotacao_db.get_by_id(10, "12345678000199")
            if cotacao:
                return "Success"
            return "Failed - No Cotacao found"
        except Exception as e:
            return f"Failed - {str(e)}"
        
    def test_get_all(self):
        try:
            self.cotacao_db.get_all()
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
        
    def test_update(self):
        try:
            cotacao = self.cotacao_db.get_by_id(10, "12345678000199")
            cotacao.valor  = 200.00
            self.cotacao_db.update(cotacao)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
        
    def test_delete(self):
        try:
            cotacao = self.cotacao_db.get_by_id(9, "12345678000199")
            self.cotacao_db.delete(cotacao)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"