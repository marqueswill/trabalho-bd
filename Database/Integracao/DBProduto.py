from Database.DBConection import Database
from Objetos.Produto import Produto


class ProdutoDB:
    def __init__(self, db):
        self.db = db

    def create_table(self):
        sql_create = """
        CREATE TABLE "tbl_produto" (
            "codProduto" serial PRIMARY KEY,
            "unidade" varchar NOT NULL,
            "quantidade" real NOT NULL,
            "nome" varchar NOT NULL,
            "descricao" varchar,
            "codCategoria" integer NOT NULL
        );
        """
        self.db.execute_query(sql_create)

    def insert(self, produto):
        sql_insert_produto = """
        INSERT INTO tbl_produto (idProduto, unidade, quantidade, descricao, idCategoria, nome)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.db.execute_query(sql_insert_produto, produto.to_tuple())

    def update(self, produto):
        sql_update_produto = """
        UPDATE tbl_produto
        SET unidade = %s, quantidade = %s, descricao = %s, idCategoria = %s, nome = %s
        WHERE idProduto = %s
        """

        params = (
            produto.unidade,
            produto.quantidade,
            produto.descricao,
            produto.idCategoria,
            produto.nome,
            produto.idProduto,
        )
        self.db.execute_query(sql_update_produto, params)

    def delete(self, idProduto):
        sql_delete_produto = """
        DELETE FROM tbl_produto
        WHERE idProduto = %s
        """
        self.db.execute_query(sql_delete_produto, (idProduto))

    def delete_all(self):
        pass

    def get_by_id(self, idProduto):
        sql_select_produto = """
        SELECT * FROM tbl_produto
        WHERE idProduto = %s
        """
        cursor = self.db.execute_query(sql_select_produto, (idProduto), fetch=True)
        if cursor:
            row = cursor
            if row:
                return Produto(*row)
        return None

    def get_all(self):
        sql_select_produtos = """
        SELECT idProduto, unidade, quantidade, descricao, idCategoria, nome
        FROM tbl_produto
        """
        cursor = self.db.execute_query(sql_select_produtos, fetch=True)
        return [Produto(*row) for row in cursor] if cursor else []
