# from Teste.TesteLote import TesteLote
# from Teste.TesteBase import TesteBase
# from Integracao.DBAjuste import DBAjuste
# from Integracao.DBProdutoEstoque import DBProdutoEstoque
# from Integracao.DBInventario import DBInventario

# from Objetos.Ajuste import Ajuste

# class TesteAjuste(TesteBase):
#     def __init__(self):
#         super().__init__()
#         self.ajuste_db = DBAjuste(teste=True)
#         self.produtoestoque_db = DBProdutoEstoque(teste=True)
#         self.inventario_db = DBInventario(teste=True)

#     def test_insert(self):
#         try:
#             produto = self.produtoestoque_db.get_by_id(1, 1)
#             inv = self.inventario_db.get_by_id(1, 1, "2024-08-01")
#             ajuste = Ajuste(
#                 valorAntigo=produto.estoqueAtual,
#                 valorNovo=inv.contagem,
#                 diferenca=produto.estoqueAtual - inv.contagem,
#                 codProduto=inv.codProduto,
#                 codEstoque=inv.codEstoque,
#                 dataInv=inv.dataInv,
#             )

#             self.ajuste_db.insert(ajuste)
#             return "Success"
#         except Exception as e:
#             return f"Failed - {str(e)}"

#     def test_get_by_id(self):
#         try:
#             ajuste = self.ajuste_db.get_by_id(1, 1, "2024-08-01")
#             if ajuste:
#                 return "Success"
#             else:
#                 return "Failed - No ajuste found"
#         except Exception as e:
#             return f"Failed - {str(e)}"

#     def test_get_all(self):
#         try:
#             self.ajuste_db.get_all()
#             return "Success"
#         except Exception as e:
#             return f"Failed - {str(e)}"

#     def test_update(self):
#         try:
#             ajuste = self.ajuste_db.get_by_id(1, 1, "2024-08-01")
#             ajuste.valorNovo = 0

#             self.ajuste_db.update(ajuste)
#             return "Success"

#         except Exception as e:
#             return f"Failed - {str(e)}"

#     def test_delete(self):
#         try:
#             self.ajuste_db.delete(1, 1, "2024-08-01")
#             return "Success"
#         except Exception as e:
#             return f"Failed - {str(e)}"
