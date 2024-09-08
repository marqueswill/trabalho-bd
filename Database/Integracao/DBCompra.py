from Database.Objetos.Compra import Compra
from Database.Integracao.DBOperation import DBOperation


class DBCompra(DBOperation):
    def __init__(self, teste=False):
        super().__init__(teste)

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
        WHERE "numNF" = %s
        """
        params = [compra.data, compra.notaFiscal, compra.numNF]
        self.db.execute_query(sql_update, params)

    def delete(self, compra):
        sql_delete = """
        DELETE FROM "Compra"
        WHERE "numNF" = %s
        """
        self.db.execute_query(sql_delete, [compra.numNF])

    def get_by_id(self, numNF):
        sql_select = """
        SELECT * FROM "Compra"
        WHERE "codOperacao" = %s AND "cnpjFornecedor" = %s AND "cnpjRestaurante" = %s
        """
        result = self.db.execute_query(sql_select, [numNF], fetch=True)
        if result:
            return Compra(*result)
        return None

    def get_all(self):
        sql_select = """
        SELECT * FROM "Compra"
        """
        results = self.db.execute_query(sql_select, fetch=True)
        return [Compra(*row) for row in results] if results else []
