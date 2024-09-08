from Database.Objetos.Funcionario import Funcionario
from Database.Integracao.DBOperation import DBOperation


class DBFuncionario(DBOperation):
    def __init__(self, teste=False):
        super().__init__(teste)

    def insert(self, funcionario: Funcionario):
        sql_insert = f"""
        INSERT INTO "Funcionario" ({",".join(funcionario.columns())})
        VALUES ({",".join(["%s"]*len(funcionario.columns()))})
        """

        self.db.execute_query(sql_insert, funcionario.to_tuple())

    def update(self, funcionario: Funcionario):
        sql_update = f"""
        UPDATE "Funcionario" 
        SET {", ".join([f"{c} = %s" for c in funcionario.columns()[:-1]])}
        WHERE "cpfFuncionario" = %s
        """
        self.db.execute_query(sql_update, funcionario.to_tuple())

    def delete(self, funcionario):
        sql_delete = """
        DELETE FROM "Funcionario"
        WHERE "cpfFuncionario" = %s
        """
        self.db.execute_query(sql_delete, [funcionario.cpfFuncionario])

    def get_by_id(self, cpfFuncionario):
        sql_select = """
        SELECT * FROM "Funcionario"
        WHERE "cpfFuncionario" = %s
        """
        result = self.db.execute_query(sql_select, [cpfFuncionario], fetch=True)
        if result:
            return Funcionario(*result)
        return None

    def get_all(self):
        sql_select = """
        SELECT *
        FROM "Funcionario"
        """
        results = self.db.execute_query(sql_select, fetch=True)
        return [Funcionario(*row) for row in results] if results else []
