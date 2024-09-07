from Teste.TesteBase import TesteBase
from Integracao.DBProdutoEstoque import DBProdutoEstoque
from Objetos.ProdutoEstoque import ProdutoEstoque

class TesteProdutoEstoque(TesteBase):
    def __init__(self):
        super().__init__()
        self.produtoEstoque_db = DBProdutoEstoque(teste=True)

    