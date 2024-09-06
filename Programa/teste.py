from Database.Integracao import *
from Database.Teste import *

dbcat = DBCategoria()

for c in dbcat.get_all():
    print(c.nome)


teste = TesteLote()
teste.run()