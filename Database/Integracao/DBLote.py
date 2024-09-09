from Database.Objetos.Lote import Lote
from Database.Integracao.DBOperation import DBOperation
from typing import List

 
class DBLote(DBOperation):

    def __init__(self, teste=False):
        super().__init__(teste)

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

    def delete(self, lote):
        sql_delete = """
        DELETE FROM "Lote"
        WHERE "numLote" = %s
        """
        self.db.execute_query(sql_delete, [lote.numLote])

    def get_by_id(self, numLote):
        l = Lote()
        sql_select = f"""
        SELECT {",".join(l.columns())} FROM "Lote"
        WHERE "numLote" = %s
        """
        result = self.db.execute_query(sql_select, [numLote], fetch=True)
        if result:
            return Lote(*result)
        return None

    def get_all(self):
        l = Lote()
        sql_select = f"""
        SELECT {",".join(l.columns())} FROM "Lote"
        """
        results = self.db.execute_query(sql_select, fetch=True)
        return [Lote(*row) for row in results] if results else []
