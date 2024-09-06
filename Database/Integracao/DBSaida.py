from Database.Objetos.Saida import Saida
from Database.Integracao.DBOperation import DBOperation


class DBSaida(DBOperation):
    def __init__(self, teste=False):
        super().__init__(teste)

    def insert(self, saida: Saida):
        sql_insert = f"""
        INSERT INTO "Saida" ({",".join(saida.columns()[:-1])})
        VALUES ({",".join(["%s"]*(len(saida.columns())-1))})
        """
        self.db.execute_query(sql_insert, saida.to_tuple()[:-1])
        return self.get_by_id(saida.to_tuple()[-1])

    def update(self, saida: Saida):
        sql_update = f"""
        UPDATE "Saida" 
        SET {", ".join([f"{c} = %s" for c in saida.columns()[:-1]])}
        WHERE "codOperacao" = %s
        """
        self.db.execute_query(sql_update, saida.to_tuple())

    def delete(self, codOperacao):
        sql_delete = """
        DELETE FROM "Saida"
        WHERE "codOperacao" = %s
        """
        self.db.execute_query(sql_delete, [codOperacao])

    def get_by_id(self, codOperacao):
        sql_select = """
        SELECT * FROM "Saida"
        WHERE "codOperacao" = %s
        """
        result = self.db.execute_query(sql_select, [codOperacao], fetch=True)
        if result:
            return Saida(*result)
        return None

    def get_all(self):
        sql_select = """
        SELECT * FROM "Saida"
        """
        results = self.db.execute_query(sql_select, fetch=True)
        return [Saida(*row) for row in results] if results else []
