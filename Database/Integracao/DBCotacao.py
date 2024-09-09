from Database.Objetos.Cotacao import Cotacao
from Database.Integracao.DBOperation import DBOperation


class DBCotacao(DBOperation):

    def __init__(self, teste=False):
        super().__init__(teste)

    def insert(self, cotacao):
        sql_insert = """
        INSERT INTO "Cotacao" ("valor", "codProduto","cnpjFornecedor")
        VALUES (%s, %s, %s)
        """
        self.db.execute_query(sql_insert, cotacao.to_tuple())

    def update(self, cotacao):
        sql_update = """
        UPDATE "Cotacao"
        SET "valor" = %s
        WHERE "codProduto" = %s AND "cnpjFornecedor" = %s
        """
        self.db.execute_query(sql_update, cotacao.to_tuple())

    def delete(self, cotacao):
        sql_delete = """
        DELETE FROM "Cotacao"
        WHERE "codProduto" = %s AND "cnpjFornecedor" = %s
        """
        self.db.execute_query(sql_delete, [cotacao.codProduto, cotacao.cnpjFornecedor,])

    def get_by_id(self, codProduto, cnpjFornecedor):
        sql_select = """
        SELECT * FROM "Cotacao"
        WHERE "codProduto" = %s AND "cnpjFornecedor" = %s
        """
        result = self.db.execute_query(sql_select, [codProduto, cnpjFornecedor], fetch=True)
        if result:
            return Cotacao(*result)
        return None
    
    def get_all(self):
        sql_select = """
        SELECT * FROM "Cotacao"
        ORDER BY "valor" ASC, "codProduto" ASC
        """
        results = self.db.execute_query(sql_select, fetch=True)
        return [Cotacao(*row) for row in results] if results else []