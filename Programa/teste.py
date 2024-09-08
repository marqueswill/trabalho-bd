from Database.Integracao import *
from Database.Teste import *


# dbEstoque = DBEstoque()

# for e in dbEstoque.get_all():
#     print(e.nome)


testes = [
    TesteCategoria(),
    TesteFuncionario(),
    TesteFornecedor(),
    TesteRestaurante(),
    TesteLote(),
    TesteEstoque(),
    TesteProdutoLote(),
    TesteEntrada(),
    TesteSaida(),
    TesteCompra(),
    TesteProdutoEstoque(),
    TesteCotacao(),
]

for t in testes:
    t.run()
