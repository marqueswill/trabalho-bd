from Objetos.Ajuste import Ajuste
from Integracao.DBOperation import DBOperation


class DBAjuste(DBOperation):

    def insert(self, ajuste: Ajuste):
        sql_insert = f"""
        INSERT INTO "Ajuste" ({",".join(ajuste.columns())})
        VALUES ({",".join(["%s"]*len(ajuste.columns()))})
        """
        self.db.execute_query(sql_insert, ajuste.to_tuple())

    def update(self, ajuste: Ajuste):
        sql_update = f"""
        UPDATE "Ajuste" 
        SET {", ".join([f"{c} = %s" for c in ajuste.columns()[:-1]])}
        WHERE "codOperacao" = %s
        """
        self.db.execute_query(sql_update, ajuste.to_tuple())

    def delete(self, codOperacao):
        sql_delete = """
        DELETE FROM "Ajuste"
        WHERE "codOperacao" = %s
        """
        self.db.execute_query(sql_delete, [codOperacao])

    def get_by_id(self, codOperacao):
        sql_select = """
        SELECT * FROM "Ajuste"
        WHERE "codOperacao" = %s
        """
        result = self.db.execute_query(sql_select, [codOperacao], fetch=True)
        if result:
            return Ajuste(*result)
        return None

    def get_all(self):
        sql_select = """
        SELECT * FROM "Ajuste"
        """
        results = self.db.execute_query(sql_select, fetch=True)
        return [Ajuste(*row) for row in results] if results else []
