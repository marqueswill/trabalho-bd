from Objetos.Inventario import Inventario
from Integracao.DBOperation import DBOperation

class DBInventario(DBOperation):

    def insert(self, inventario: Inventario):
        sql_insert_inventario = """
        INSERT INTO "Inventario" (codProduto, codEstoque, data, contagem, diferenca, ajustado, cpfOperador)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        self.db.execute_querey(sql_insert_inventario, inventario.to_tuple())

    def delete(self, codProduto, codEstoque, dataInv):
        sql_delete_inventario = """
        DELETE FROM "Inventario"
        WHERE codProduto = %s AND codEstoque = %s AND dataInv = %s
        """
        self.db.execute_querey(sql_delete_inventario, codProduto, codEstoque, dataInv)

    def get_one(self, codProduto, codEstoque, dataInv):
        sql_select_inventario = """
        SELECT * FROM "Inventario"
        WHERE codProduto = %s AND codEstoque = %s AND dataInv = %s
        """

        cursor = self.db.execute_querey(sql_select_inventario, codProduto, codEstoque, dataInv, fetchone=True)
        if cursor:
            row = cursor
            if row:
                return Inventario(*row)
        return None

    def get_all(self):
        sql_select_inventarios = """
        SELECT codProduto, codEstoque, dataInv, contagem, diferenca, ajustado, cpfOperador
        FROM "Inventario"
        """

        cursor = self.db.execute_querey(sql_select_inventarios, fetch=True)
        return [Inventario(*row) for row in cursor] if cursor else []
