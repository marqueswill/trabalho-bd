from Database.Integracao import *
from Database.Teste import *

dbcat = DBProdutoEstoque()

for c in dbcat.get_all():
    print(c.ultimoInv)


teste = TesteProdutoEstoque()
teste.run()