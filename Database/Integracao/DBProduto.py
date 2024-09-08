from Database.Objetos.Produto import Produto
from Database.Integracao.DBOperation import DBOperation


class DBProduto(DBOperation):

    def insert(self, produto):
        sql_insert_produto = """
        INSERT INTO "Produto" ("codProduto","unidade", "quantidade", "nome", "descricao", "codCategoria")
        VALUES (%s,%s, %s, %s, %s, %s)
        """
        self.db.execute_query(sql_insert_produto, produto.to_tuple())

    def update(self, produto):
        sql_update_produto = """
        UPDATE "Produto"
        SET "unidade" = %s, "quantidade" = %s, "descricao" = %s, "codCategoria" = %s, "nome" = %s
        WHERE "codProduto" = %s
        """

        params = (
            produto.unidade,
            produto.quantidade,
            produto.descricao,
            produto.idCategoria,
            produto.nome,
            produto.idProduto,
        )
        self.db.execute_query(sql_update_produto, [params])

    def delete(self, produto):
        print("produto",produto)
        sql_delete_produto = """
        DELETE FROM "Produto"
        WHERE "codProduto" = %s
        """
        self.db.execute_query(sql_delete_produto, [produto.idProduto])

    def get_by_id(self, idProduto):
        sql_select_produto = """
        SELECT * FROM "Produto"
        WHERE "codProduto" = %s
        """
        cursor = self.db.execute_query(sql_select_produto, [idProduto], fetch=True)
        if cursor:
            row = cursor
            if row:
                return Produto(*row)
        return None

    def get_all(self):
        sql_select_produtos = """
        SELECT "codProduto", "unidade", "quantidade", "descricao", "codCategoria", "nome"
        FROM "Produto"
        """
        cursor = self.db.execute_query(sql_select_produtos, fetch=True)
        return [Produto(*row) for row in cursor] if cursor else []
