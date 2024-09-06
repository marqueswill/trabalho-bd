from Objetos.Estoque import Estoque
from Integracao.DBOperation import DBOperation

class DBEstoque(DBOperation):
    def create_table(self):
        sql_create = """
        CREATE TABLE "Estoque" (
            "codEstoque" integer PRIMARY KEY,
            "nome" varchar not null,
            "cnpjRestaurante" char(14) not null
        );
        """
        self.db.execute_query(sql_create)

    def insert(self, estoque):
        sql_insert = """
        INSERT INTO "Estoque" ("codEstoque","nome","cnpjRestaurante")
        VALUES (%s, %s, %s)
        """
        self.db.execute_query(sql_insert, estoque.to_tuple())

    def update(self, estoque):
        sql_update = """
        UPDATE "Estoque"
        SET "nome" = %s, "cnpjRestaurante" = %s
        WHERE "codEstoque" = %s
        """
        self.db.execute_query(sql_update, estoque.to_tuple())