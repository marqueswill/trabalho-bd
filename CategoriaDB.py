from DBConection import Database
from Categoria import Categoria


class CategoriaDB:

    def __init__(self, db):
        self.db = db

    def create_table(self):
        sql_create = ("""
            CREATE TABLE IF NOT EXISTS tbl_categoria (
            idCategoria INT, 
            nome VARCHAR(45), 
            PRIMARY KEY (idCategoria))
            """)

        self.db.execute_query(sql_create)

    def insert_categoria(self, categoria):
        sql_insert = """
        INSERT INTO tbl_categoria (idCategoria, nome)
        VALUES (%s, %s)
        """
        self.db.execute_query(sql_insert, categoria.to_tuple())

    def update_categoria(self, categoria):
        sql_update = """
        UPDATE tbl_categoria 
        SET nome = %s 
        WHERE idCategoria = %s
        """
        params = (categoria.nome, categoria.idCategoria)
        self.db.execute_query(sql_update, params)

    def delete_categoria(self, idCategoria):
        sql_delete = """
        DELETE FROM tbl_categoria
        WHERE idCategoria = %s
        """
        self.db.execute_query(sql_delete, (idCategoria,))

    def get_categoria_by_id(self, idCategoria):
        sql_select = """
        SELECT idCategoria, nome 
        FROM tbl_categoria
        WHERE idCategoria = %s
        """
        result = self.db.execute_query(sql_select, (idCategoria,), fetch=True)
        if result:
            return Categoria(*result)
        return None

    def get_all_categorias(self):
        sql_select = """
            SELECT * FROM tbl_categoria
        """

        results = self.db.execute_query(sql_select, fetch=True)
        return [Categoria(*row) for row in results] if results else []


