from Objetos.Entrada import Entrada
from Integracao.DBOperation import DBOperation


class DBEntrada(DBOperation):

    def insert(self, entrada: Entrada):
        sql_insert = f"""
        INSERT INTO "Entrada" ({",".join(entrada.columns())})
        VALUES ({",".join(["%s"]*len(entrada.columns()))})
        """
        self.db.execute_query(sql_insert, entrada.to_tuple())

    def update(self, entrada: Entrada):
        sql_update = f"""
        UPDATE "Entrada" 
        SET {", ".join([f"{c} = %s" for c in entrada.columns()[:-1]])}
        WHERE "codOperacao" = %s
        """
        self.db.execute_query(sql_update, entrada.to_tuple())

    def delete(self, codOperacao):
        sql_delete = """
        DELETE FROM "Entrada"
        WHERE "codOperacao" = %s
        """
        self.db.execute_query(sql_delete, [codOperacao])

    def get_by_id(self, codOperacao):
        sql_select = """
        SELECT * FROM "Entrada"
        WHERE "codOperacao" = %s
        """
        result = self.db.execute_query(sql_select, [codOperacao], fetch=True)
        if result:
            return Entrada(*result)
        return None

    def get_all(self):
        sql_select = """
        SELECT * FROM "Entrada"
        """
        results = self.db.execute_query(sql_select, fetch=True)
        return [Entrada(*row) for row in results] if results else []
