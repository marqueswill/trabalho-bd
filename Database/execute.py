from DBConection import Database
from Integracao.DBOperation import DBOperation
from Teste.TesteLote import TesteLote
from Teste.TesteProdutoLote import TesteProdutoLote
from Teste.TesteSaida import TesteSaida
from Teste.TesteFuncionario import TesteFuncionario
from Teste.TesteEntrada import TesteEntrada
from Teste.TesteCompra import TesteCompra
# from Teste.TesteAjuste import TesteAjuste

db = DBOperation()
db.reset()
db.seed()

teste_compra = TesteCompra()
teste_compra.run()

# teste_funcionario = TesteFuncionario()
# teste_funcionario.run()

# teste_lote = TesteLote()
# teste_lote.run()

# teste_saida = TesteSaida()
# teste_saida.run()

# teste_entrada = TesteEntrada()
# teste_entrada.run()

# teste_ajuste = TesteAjuste()
# teste_ajuste.run()