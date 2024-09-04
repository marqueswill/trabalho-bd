from Database.Integracao.DBOperation import DBOperation
from Database.Objetos.Fornecedor import Fornecedor




class DBFornecedor(DBOperation):
    def __init__(self, teste=False):
        super().__init__(teste)

    def create_table(self):
        sql_create = """
        CREATE TABLE "Fornecedor" (
            "cnpjFornecedor" char(14) PRIMARY KEY,
            "endereco" varchar,
            "razao" varchar NOT NULL UNIQUE,
            "nome" varchar NOT NULL,
            "telefone" bigint
        );
        """
        self.db.execute_query(sql_create)

    def insert(self, fornecedor: Fornecedor):
        sql_insert = f"""
        INSERT INTO "Fornecedor" ({",".join(fornecedor.columns())})
        VALUES ({",".join(["%s"] * len(fornecedor.columns()))})
        """
        # print(sql_insert)
        self.db.execute_query(sql_insert, fornecedor.to_tuple())

    def update(self, fornecedor: Fornecedor):
        sql_update = f"""
        UPDATE "Fornecedor" 
        SET {", ".join([f"{c} = %s" for c in fornecedor.columns()[:-1]])}
        WHERE "cnpjFornecedor" = %s
        """
        self.db.execute_query(sql_update, fornecedor.to_tuple())

    def delete(self, cnpjFornecedor):
        sql_delete = """
        DELETE FROM "Fornecedor"
        WHERE "cnpjFornecedor" = %s
        """
        self.db.execute_query(sql_delete, [cnpjFornecedor])
    
    def delete_all(self):
        pass

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


