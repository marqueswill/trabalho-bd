from Database.Objetos.Categoria import Categoria
from Database.Integracao.DBOperation import DBOperation


class DBCategoria(DBOperation):

    def __init__(self, teste=False):
        super().__init__(teste)

    def insert(self, categoria: Categoria):
        sql_insert = """
        INSERT INTO "Categoria" ("nome")
        VALUES (%s)
        """
        self.db.execute_query(sql_insert, [categoria.nome])

    def update(self, categoria: Categoria):
        sql_update = """
        UPDATE "Categoria" 
        SET nome = %s 
        WHERE "codCategoria" = %s
        """
        params = (categoria.nome, categoria.codCategoria)
        self.db.execute_query(sql_update, params)

    def delete(self, categoria: Categoria):
        sql_delete = """
        DELETE FROM "Categoria"
        WHERE "codCategoria" = %s
        """
        self.db.execute_query(sql_delete, [categoria.codCategoria])

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
