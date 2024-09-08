from Database.Integracao.DBCompra import DBCompra
from Database.Integracao.DBOperation import DBOperation
from Front.telas import TelaInicial

# faz setup da database (reset e seed)
db = DBOperation()
db.setup()

# Substituir dummy data da seed  
db_compra = DBCompra()
compras = db_compra.get_all()

pdf_exemplo = db_compra.get_as_bytea("./Input/nota-fiscal.pdf")

for c in compras:
    c.notaFiscal = pdf_exemplo
    db_compra.update(c)

# roda o programa
while True:
    TelaInicial()
