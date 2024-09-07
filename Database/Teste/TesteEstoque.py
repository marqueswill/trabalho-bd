from Teste.TesteBase import TesteBase
from Integracao.DBEstoque import DBEstoque
from Objetos.Estoque import Estoque

class TesteEstoque(TesteBase):
    def __init__(self):
        super().__init__()
        self.estoque_db = DBEstoque(teste=True)

    def test_insert(self):
        try:
            estoques = [
                Estoque(codEstoque= 1, nome="Estoque 1" ,cnpjRestaurante="98765432000199"),
                Estoque(codEstoque= 2, nome="Estoque 2" ,cnpjRestaurante="98765432000199")
            ]
            for estoque in estoques:
                self.estoque_db.insert(estoque)
            return "Success"
        except Exception as e:
            f"Failed - {str(e)}"

    def test_get_by_id(self):
        try:
            estoque = self.estoque_db.get_by_id(1)
            if estoque:
                return "Success"
            else:
                return "Failed - No Estoque found"
        except Exception as e:
            return f"Failed - {str(e)}"
    
    def test_get_all(self):
        try:
            select_all = self.estoque_db.get_all()
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
        
    def test_delete(self):
        try:
            self.estoque_db.delete(1)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"