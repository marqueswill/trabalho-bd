from Database.Integracao import *
from Database.Teste.TesteInventario import TesteInventario


# dbEstoque = DBEstoque()

# for e in dbEstoque.get_all():
#     print(e.nome)


testes = [
    TesteCategoria(),
    TesteFuncionario(),
    TesteFornecedor(),
    TesteRestaurante(),
    TesteEstoque(),
    TesteLote(),
    TesteProdutoLote(),
    # TesteEntrada(),
    # TesteSaida(),
    # TesteCompra(),
]

for t in testes:
    t.run()
