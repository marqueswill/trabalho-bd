from Database.Integracao import *
from Database.Teste import *

dbEstoque = DBEstoque()

for e in dbEstoque.get_all():
    print(e.nome)


teste = TesteLote()
teste.run()