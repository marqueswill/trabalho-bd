from Database.Integracao import *
from Database.Teste.TesteInventario import TesteInventario

dbInventario = DBInventario()

for e in dbInventario.get_all():
    print(e.codEstoque)


teste = TesteInventario()
teste.run()