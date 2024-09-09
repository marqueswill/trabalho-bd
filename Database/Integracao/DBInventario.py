from Database.Objetos.Inventario import Inventario
from Database.Integracao.DBOperation import DBOperation


class DBInventario(DBOperation):

    def insert(self, inventario: Inventario):
        sql_insert_inventario = f"""
        INSERT INTO "Inventario" ({",".join(inventario.columns())})
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        # print(sql_insert_inventario, inventario.to_tuple())
        self.db.execute_query(sql_insert_inventario, inventario.to_tuple())

    def update(self, inventario: Inventario):
        sql_update = """
        UPDATE "Inventario"
        SET "contagem" = %s, "diferenca" = %s, "ajustado" = %s, "cpfEstoquista" = %s
        WHERE "codProduto" = %s AND "codEstoque" = %s AND "data" = %s
        """
        # print(sql_update, inventario.to_tuple())
        self.db.execute_query(sql_update, inventario.to_tuple())

    def delete(self, codProduto, codEstoque, data):
        sql_delete_inventario = """
        DELETE FROM "Inventario"
        WHERE "codProduto" = %s AND "codEstoque" = %s AND "data" = %s
        """
        self.db.execute_query(sql_delete_inventario, [codProduto, codEstoque, data])

    def get_by_id(self, codProduto, codEstoque, data):
        i = Inventario()
        sql_select_inventario = f"""
        SELECT {",".join(i.columns())} FROM "Inventario"
        WHERE "codProduto" = %s AND "codEstoque" = %s AND "data" = %s
        """

        cursor = self.db.execute_query(
            sql_select_inventario, [codProduto, codEstoque, data], fetch=True
        )
        if cursor:
            row = cursor
            if row:
                return Inventario(*row)
        return None

    def get_all(self):
        i = Inventario()
        sql_select_inventarios = f"""
        SELECT {",".join(i.columns())} FROM "Inventario"
        ORDER BY "data"
        """

        cursor = self.db.execute_query(sql_select_inventarios, fetch=True)
        return [Inventario(*row) for row in cursor] if cursor else []
