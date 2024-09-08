from Database.Objetos.Produto import Produto
from Database.Integracao.DBOperation import DBOperation


class DBProduto(DBOperation):

    def insert(self, produto):
        sql_insert = """
        INSERT INTO "Produto" ("nome", "quantidade","unidade",  "descricao", "codCategoria")
        VALUES (%s, %s, %s, %s, %s)
        """
        self.db.execute_query(sql_insert, produto.to_tuple()[:-1])

    def update(self, produto):
        sql_update = """
        UPDATE "Produto"
        SET "nome" = %s,"quantidade" = %s,"unidade" = %s,   "descricao" = %s, "codCategoria" = %s
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
        p = Produto()
        sql_select = f"""
        SELECT {",".join(p.columns())} FROM "Produto"
        WHERE "codProduto" = %s
        """
        cursor = self.db.execute_query(sql_select, [codProduto], fetch=True)
        if cursor:
            row = cursor
            if row:
                return Produto(*row)
        return None

    def get_all(self):
        p = Produto()
        sql_select = f"""
        SELECT {",".join(p.columns())} FROM "Produto"
        """
        results = self.db.execute_query(sql_select, fetch=True)
        return [Produto(*row) for row in results] if results else []
