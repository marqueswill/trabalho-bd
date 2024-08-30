from Objetos.Lote import Lote
from Integracao.DBOperation import DBOperation
from typing import List


class DBLote(DBOperation):
    def create_table(self):
        sql_create = """
        CREATE TABLE "Lote" (
        "numLote" serial PRIMARY KEY,
        "tipo" varchar
        );
        """
        self.db.execute_query(sql_create)

    def insert(self, lote: Lote):
        sql_insert = f"""
        INSERT INTO "Lote" ({",".join(lote.columns()[:-1])})
        VALUES ({", ".join(["%s"]*(len(lote.columns())-1))})
        """
        self.db.execute_query(sql_insert, lote.to_tuple()[:-1])

    def update(self, lote: Lote):
        sql_update = """
        UPDATE "Lote"
        SET "tipo" = %s
        WHERE "numLote" = %s
        """

        self.db.execute_query(sql_update, lote.to_tuple())

    def delete(self, numLote):
        sql_delete = """
        DELETE FROM "Lote"
        WHERE "numLote" = %s
        """
        self.db.execute_query(sql_delete, [numLote])

    def delete_all(self):
        sql_delete_all = """
        DELETE FROM "Lote"
        """
        self.db.execute_query(sql_delete_all)

    def get_by_id(self, numLote):
        sql_select = """
        SELECT * FROM "Lote" 
        WHERE "numLote" = %s
        """
        result = self.db.execute_query(sql_select, [numLote], fetch=True)
        if result:
            return Lote(*result)
        return None

    def get_all(self):
        sql_select = """
        SELECT "numLote", "tipo" FROM "Lote"
        """
        results = self.db.execute_query(sql_select, fetch=True)
        return [Lote(*row) for row in results] if results else []
