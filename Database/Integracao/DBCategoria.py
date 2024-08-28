from Database.DBConection import Database
from Objetos.Categoria import Categoria


class DBCategoria:
    def __init__(self, db):
        self.db = db

    def create_table(self):
        sql_create = """
        CREATE TABLE "tbl_categoria" (
            "codCategoria" serial PRIMARY KEY,
            "nome" varchar NOT NULL
        );
        """

        self.db.execute_query(sql_create)

    def insert(self, categoria):
        sql_insert = """
        INSERT INTO tbl_categoria (idCategoria, nome)
        VALUES (%s, %s)
        """
        self.db.execute_query(sql_insert, categoria.to_tuple())

    def update(self, categoria):
        sql_update = """
        UPDATE tbl_categoria 
        SET nome = %s 
        WHERE idCategoria = %s
        """
        params = (categoria.nome, categoria.idCategoria)
        self.db.execute_query(sql_update, params)

    def delete(self, idCategoria):
        sql_delete = """
        DELETE FROM tbl_categoria
        WHERE idCategoria = %s
        """
        self.db.execute_query(sql_delete, (idCategoria,))

    def delete_all(self):
        pass

    def get_by_id(self, idCategoria):
        sql_select = """
        SELECT * FROM tbl_categoria
        WHERE idCategoria = %s
        """
        result = self.db.execute_query(sql_select, (idCategoria,), fetch=True)
        if result:
            return Categoria(*result)
        return None

    def get_all(self):
        sql_select = """
            SELECT * FROM tbl_categoria
        """

        results = self.db.execute_query(sql_select, fetch=True)
        return [Categoria(*row) for row in results] if results else []
