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
    TesteProdutoEstoque(),
    TesteProduto(),
    TesteCotacao(),
    TesteInventario(),
    TesteCompra(),
]

for t in testes:
    t.run()
