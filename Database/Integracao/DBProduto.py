from Database.Objetos.Produto import Produto
from Database.Integracao.DBOperation import DBOperation


class DBProduto(DBOperation):

    def insert(self, produto):
        sql_insert = """
        INSERT INTO "Produto" ("unidade", "quantidade", "nome", "descricao", "codCategoria","codProduto")
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.db.execute_query(sql_insert, produto.to_tuple())

    def update(self, produto):
        sql_update = """
        UPDATE "Produto"
        SET "unidade" = %s, "quantidade" = %s, "nome" = %s, "descricao" = %s, "codCategoria" = %s
        WHERE "codProduto" = %s
        """
        self.db.execute_query(sql_update, produto.to_tuple())

    def delete(self, produto):
        sql_delete = """
        DELETE FROM "Produto"
        WHERE "codProduto" = %s
        """
        self.db.execute_query(sql_delete, [produto.codProduto])

    def get_by_id(self, codProduto):
        sql_select = """
        SELECT * FROM "Produto"
        WHERE "codProduto" = %s
        """
        cursor = self.db.execute_query(sql_select, [codProduto], fetch=True)
        if cursor:
            row = cursor
            if row:
                return Produto(*row)
        return None

    def get_all(self):
        sql_select= """
        SELECT * FROM "Produto"
        """
        results = self.db.execute_query(sql_select, fetch=True)
        return [Produto(*row) for row in results] if results else []
