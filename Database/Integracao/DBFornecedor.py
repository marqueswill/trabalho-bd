from Database.Integracao.DBOperation import DBOperation
from Database.Objetos.Fornecedor import Fornecedor


class DBFornecedor(DBOperation):
    def __init__(self, teste=False):
        super().__init__(teste)

    def insert(self, fornecedor: Fornecedor):
        sql_insert = f"""
        INSERT INTO "Fornecedor" ({",".join(fornecedor.columns())})
        VALUES ({",".join(["%s"] * len(fornecedor.columns()))})
        """
        self.db.execute_query(sql_insert, fornecedor.to_tuple())

    def update(self, fornecedor: Fornecedor):
        sql_update = f"""
        UPDATE "Fornecedor" 
        SET {", ".join([f"{c} = %s" for c in fornecedor.columns()[:-1]])}
        WHERE "cnpjFornecedor" = %s
        """
        self.db.execute_query(sql_update, fornecedor.to_tuple())

    def delete(self, fornecedor):
        sql_delete = """
        DELETE FROM "Fornecedor"
        WHERE "cnpjFornecedor" = %s
        """
        self.db.execute_query(sql_delete, [fornecedor.cnpjFornecedor])

    def get_by_id(self, cnpjFornecedor):
        sql_select = """
        SELECT * FROM "Fornecedor"
        WHERE "cnpjFornecedor" = %s
        """
        result = self.db.execute_query(sql_select, [cnpjFornecedor], fetch=True)
        if result:
            return Fornecedor(*result)
        return None

    def get_all(self):
        sql_select = """
        SELECT
            "cnpjFornecedor",
            "endereco",
            "razao",
            "nome",
            "telefone"
        FROM "Fornecedor"
        """
        results = self.db.execute_query(sql_select, fetch=True)
        return [Fornecedor(*row) for row in results] if results else []
