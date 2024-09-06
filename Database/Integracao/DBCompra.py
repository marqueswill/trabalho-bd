from Objetos.Compra import Compra
from Integracao.DBOperation import DBOperation


class DBCompra(DBOperation):
    def create_table(self):
        sql_create = """
        CREATE TABLE "Compra" (
            "codOperacao" integer,
            "cnpjFornecedor" char(14),
            "cnpjRestaurante" char(14),
            "notaFiscal" bytea not null,
            "data" date not null,
            PRIMARY KEY ("codOperacao", "cnpjFornecedor", "cnpjRestaurante")
        );
        """
        self.db.execute_query(sql_create)

    def insert(self, compra):
        sql_insert = """
        INSERT INTO "Compra" ("data","notaFiscal","codOperacao", "cnpjFornecedor","cnpjRestaurante")
        VALUES (%s, %s, %s, %s, %s)
        """
        self.db.execute_query(sql_insert, compra.to_tuple())

    def update(self, compra):
        sql_update = """
        UPDATE "Compra" 
        SET "data" = %s, "notaFiscal" = %s
        WHERE "codOperacao" = %s AND "cnpjFornecedor" = %s AND "cnpjRestaurante" = %s
        """
        params = (compra.codOperacao, compra.cnpjFornecedor, compra.cnpjRestaurante)
        self.db.execute_query(sql_update, compra.to_tuple())

    def delete(self, codOperacao, cnpjFornecedor, cnpjRestaurante):
        sql_delete = """
        DELETE FROM "Compra"
        WHERE "codOperacao" = %s AND "cnpjFornecedor" = %s AND "cnpjRestaurante" = %s
        """
        self.db.execute_query(
            sql_delete, [codOperacao, cnpjFornecedor, cnpjRestaurante]
        )

    def delete_all(self):
        # Implementation for deleting all categories
        pass

    def get_by_id(self, codOperacao, cnpjFornecedor, cnpjRestaurante):
        sql_select = """
        SELECT * FROM "Compra"
        WHERE "codOperacao" = %s AND "cnpjFornecedor" = %s AND "cnpjRestaurante" = %s
        """
        result = self.db.execute_query(
            sql_select, [codOperacao, cnpjFornecedor, cnpjRestaurante], fetch=True
        )
        if result:
            return Compra(*result)
        return None

    def get_all(self):
        sql_select = """
        SELECT * FROM "Compra"
        """
        results = self.db.execute_query(sql_select, fetch=True)
        return [Compra(*row) for row in results] if results else []
