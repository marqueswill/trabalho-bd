from Objetos.ProdutoLote import ProdutoLote
from Integracao.DBOperation import DBOperation


class DBProdutoLote(DBOperation):

    def create_table(self):
        sql_create = """
        CREATE TABLE "ProdutoLote" (
        "codProduto" integer,
        "codEstoque" integer,
        "numLote" integer,
        "quantidade" integer NOT NULL,
        PRIMARY KEY ("codProduto", "codEstoque", "numLote")
        );
        """
        self.db.execute_query(sql_create)

    def insert(self, produtolote: ProdutoLote):
        sql_insert = f"""
        INSERT INTO "ProdutoLote" ({",".join(produtolote.columns())})
        VALUES ({",".join(["%s"]*len(produtolote.columns()))})
        """
        self.db.execute_query(sql_insert, produtolote.to_tuple())

    def update(self, produtolote: ProdutoLote):
        sql_update = f"""
        UPDATE "ProdutoLote" 
        SET {", ".join([f"{c} = %s" for c in produtolote.columns()[:-3]])}
        WHERE "codProduto" = %s AND "codEstoque" = %s AND "numLote" = %s
        """

        self.db.execute_query(sql_update, produtolote.to_tuple())

    def delete(self, codProduto,codEstoque,numLote):
        sql_delete = """
        DELETE FROM "ProdutoLote"
        WHERE "codProduto" = %s AND "codEstoque" = %s AND "numLote" = %s
        """
        self.db.execute_query(sql_delete, [codProduto, codEstoque, numLote])

    def delete_all(self):
        sql_delete_all = """
        DELETE FROM "ProdutoLote"
        """
        self.db.execute_query(sql_delete_all)

    def get_by_id(self, codProduto, codEstoque, numLote):
        sql_select = """
        SELECT * FROM "ProdutoLote"
        WHERE "codProduto" = %s AND "codEstoque" = %s AND "numLote" = %s
        """
        result = self.db.execute_query(
            sql_select, [codProduto, codEstoque, numLote], fetch=True
        )
        if result:
            return ProdutoLote(*result)
        return None

    def get_all(self):
        sql_select = """
        SELECT * FROM "ProdutoLote"
        """
        results = self.db.execute_query(sql_select, fetch=True)
        return [ProdutoLote(*row) for row in results] if results else []
