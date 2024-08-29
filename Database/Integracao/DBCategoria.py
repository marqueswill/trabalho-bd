from Objetos.Categoria import Categoria
from Integracao.DBOperation import DBOperation

class DBCategoria(DBOperation):
    def create_table(self):
        sql_create = """
        CREATE TABLE "Categoria" (
            "codCategoria" serial PRIMARY KEY,
            "nome" varchar NOT NULL
        );
        """
        self.db.execute_query(sql_create)

    def insert(self, categoria):
        sql_insert = """
        INSERT INTO "Categoria" ("codCategoria", "nome")
        VALUES (%s, %s)
        """
        self.db.execute_query(sql_insert, categoria.to_tuple())

    def update(self, categoria):
        sql_update = """
        UPDATE "Categoria" 
        SET nome = %s 
        WHERE codCategoria = %s
        """
        params = (categoria.nome, categoria.codCategoria)
        self.db.execute_query(sql_update, params)

    def delete(self, codCategoria):
        sql_delete = """
        DELETE FROM "Categoria"
        WHERE "codCategoria" = %s
        """
        self.db.execute_query(sql_delete, [codCategoria])

    def delete_all(self):
        # Implementation for deleting all categories
        pass

    def get_by_id(self, codCategoria):
        sql_select = """
        SELECT * FROM "Categoria"
        WHERE "codCategoria" = %s
        """
        result = self.db.execute_query(sql_select, [codCategoria], fetch=True)
        if result:
            return Categoria(*result)
        return None

    def get_all(self):
        sql_select = """
        SELECT "codCategoria", "nome" FROM "Categoria"
        """
        results = self.db.execute_query(sql_select, fetch=True)
        return [Categoria(*row) for row in results] if results else []
