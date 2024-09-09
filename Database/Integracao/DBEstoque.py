from Database.Objetos.Estoque import Estoque
from Database.Integracao.DBOperation import DBOperation


class DBEstoque(DBOperation):

    def __init__(self, teste=False):
        super().__init__(teste)

    def insert(self, estoque: Estoque):
        sql_insert = """
        INSERT INTO "Estoque" ("nome","cnpjRestaurante")
        VALUES (%s, %s)
        """
        self.db.execute_query(sql_insert, estoque.to_tuple()[:-1])

    def update(self, estoque: Estoque):
        sql_update = """
        UPDATE "Estoque"
        SET "nome" = %s, "cnpjRestaurante" = %s
        WHERE "codEstoque" = %s
        """
        self.db.execute_query(sql_update, estoque.to_tuple())

    def delete(self, estoque: Estoque):
        sql_delete = """
        DELETE FROM "Estoque"
        WHERE "codEstoque" = %s
        """
        self.db.execute_query(sql_delete, [estoque.codEstoque])

    def get_by_id(self, codEstoque):
        e = Estoque()
        sql_select = f"""
        SELECT {",".join(e.columns())} FROM "Estoque"
        WHERE "codEstoque" = %s
        """
        # print(sql_select, [codEstoque])
        result = self.db.execute_query(sql_select, [codEstoque], fetch=True)
        if result:
            return Estoque(*result)
        return None

    def get_all(self):
        e = Estoque()
        sql_select = f"""
        SELECT {",".join(e.columns())} FROM "Estoque"
        ORDER BY "codEstoque"
        """
        results = self.db.execute_query(sql_select, fetch=True)
        return [Estoque(*row) for row in results] if results else []
