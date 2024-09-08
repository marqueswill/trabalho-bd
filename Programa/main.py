from Database.Integracao.DBOperation import DBOperation
from Front.telas import TelaInicial

# faz setup da database (reset e seed)
db = DBOperation()
db.setup()

# roda o programa
while True:
    TelaInicial()
