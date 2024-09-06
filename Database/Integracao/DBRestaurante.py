from Database.Integracao.DBOperation import DBOperation
from Database.Objetos.Restaurante import Restaurante


class DBRestaurante(DBOperation):
    def __init__(self, teste=False):
        super().__init__(teste)

    def insert(self, restaurante: Restaurante):
        sql_insert = f"""
        INSERT INTO "Restaurante" ({",".join(restaurante.columns())})
        VALUES ({",".join(["%s"] * len(restaurante.columns()))})
        """
        self.db.execute_query(sql_insert, restaurante.to_tuple())

    def update(self, restaurante: Restaurante):
        sql_update = f"""
        UPDATE "Restaurante" 
        SET {", ".join([f"{c} = %s" for c in restaurante.columns()[:-1]])}
        WHERE "cnpjRestaurante" = %s
        """
        self.db.execute_query(sql_update, restaurante.to_tuple())

    def delete(self, cnpjRestaurante):
        sql_delete = """
        DELETE FROM "Restaurante"
        WHERE "cnpjRestaurante" = %s
        """
        self.db.execute_query(sql_delete, [cnpjRestaurante])

    def get_by_id(self, cnpjRestaurante):
        sql_select = """
        SELECT * FROM "Restaurante"
        WHERE "cnpjRestaurante" = %s
        """
        result = self.db.execute_query(sql_select, [cnpjRestaurante], fetch=True)
        if result:
            return Restaurante(*result)
        return None

    def get_all(self):
        sql_select = """
        SELECT
            "cnpjRestaurante",
            "endereco",
            "razao",
            "nome",
            "telefone",
            "cnpjMatriz",
            "cpfGerente"
        FROM "Restaurante"
        """
        results = self.db.execute_query(sql_select, fetch=True)
        return [Restaurante(*row) for row in results] if results else []
