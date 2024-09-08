from Database.Objetos.ProdutoLote import ProdutoLote
from Database.Integracao.DBOperation import DBOperation


class DBProdutoLote(DBOperation):

    def __init__(self, teste=False):
        super().__init__(teste)

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

    def delete(self, produtolote):
        sql_delete = """
        DELETE FROM "ProdutoLote"
        WHERE "codProduto" = %s AND "codEstoque" = %s AND "numLote" = %s
        """
        self.db.execute_query(
            sql_delete,
            [produtolote.codProduto, produtolote.codEstoque, produtolote.numLote],
        )

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
        pl = ProdutoLote()
        sql_select = f"""
        SELECT {",".join(pl.columns())} FROM "ProdutoLote"
        """
        results = self.db.execute_query(sql_select, fetch=True)
        return [ProdutoLote(*row) for row in results] if results else []
