from Database.Objetos.Inventario import Inventario
from Database.Integracao.DBOperation import DBOperation

class DBInventario(DBOperation):

    def insert(self, inventario: Inventario):
        sql_insert_inventario = """
        INSERT INTO "Inventario" ("codProduto", "codEstoque", "data", "contagem", "diferenca", "ajustado", "cpfOperador")
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        self.db.execute_query(sql_insert_inventario, inventario.to_tuple())

    def delete(self, codProduto, codEstoque, data):
        sql_delete_inventario = """
        DELETE FROM "Inventario"
        WHERE "codProduto" = %s AND "codEstoque" = %s AND "data" = %s
        """
        self.db.execute_query(sql_delete_inventario, [codProduto, codEstoque, data])

    def get_one(self, codProduto, codEstoque, data):
        sql_select_inventario = """
        SELECT * FROM "Inventario"
        WHERE "codProduto" = %s AND "codEstoque" = %s AND "data" = %s
        """

        cursor = self.db.execute_query(sql_select_inventario, [codProduto, codEstoque, data], fetch=True)
        if cursor:
            row = cursor
            if row:
                return Inventario(*row)
        return None

    def get_all(self):
        sql_select_inventarios = """
        SELECT "codProduto", "codEstoque", "data", "contagem", "diferenca", "ajustado", "cpfOperador"
        FROM "Inventario"
        """

        cursor = self.db.execute_query(sql_select_inventarios, fetch=True)
        return [Inventario(*row) for row in cursor] if cursor else []
