from Database.Objetos.ProdutoEstoque import ProdutoEstoque
from Database.Integracao.DBOperation import DBOperation


class DBProdutoEstoque(DBOperation):

    def __init__(self, teste=False):
        super().__init__(teste)

    def insert(self, produtoEstoque):
        sql_insert = """
        INSERT INTO "ProdutoEstoque" ("estoqueMax","estoqueMin","estoqueAtual","estoqueDisp","ultimoInv","codProduto","codEstoque")
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        self.db.execute_query(sql_insert, produtoEstoque.to_tuple())

    def update(self, produtoEstoque):
        sql_update = """
        UPDATE "ProdutoEstoque"
        SET "estoqueMax" = %s, "estoqueMin" = %s, "estoqueAtual" = %s, "estoqueDisp" = %s, "ultimoInv" = %s
        WHERE "codProduto" = %s AND "codEstoque" = %s
        """
        self.db.execute_query(sql_update, produtoEstoque.to_tuple())

    def delete(self, produtoEstoque):
        sql_delete = """
        DELETE FROM "ProdutoEstoque"
        WHERE "codProduto" = %s AND "codEstoque" = %s
        """
        self.db.execute_query(
            sql_delete,
            [
                produtoEstoque.codProduto,
                produtoEstoque.codEstoque,
            ],
        )

    def get_by_id(self, codProduto, codEstoque):
        sql_select = """
        SELECT * FROM "ProdutoEstoque"
        WHERE "codProduto" = %s AND "codEstoque" = %s
        """
        result = self.db.execute_query(sql_select, [codProduto, codEstoque], fetch=True)
        if result:
            return ProdutoEstoque(*result)
        return None

    def get_all(self):
        sql_select = """
        SELECT * FROM "ProdutoEstoque"
        """
        results = self.db.execute_query(sql_select, fetch=True)
        return [ProdutoEstoque(*row) for row in results] if results else []
