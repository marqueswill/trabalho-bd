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
        # print(sql_update, funcionario.to_tuple())
        self.db.execute_query(sql_update, funcionario.to_tuple())

    def delete(self, funcionario):
        sql_delete = """
        DELETE FROM "Funcionario"
        WHERE "cpfFuncionario" = %s
        """
        self.db.execute_query(sql_delete, [funcionario.cpfFuncionario])

    def get_by_id(self, cpfFuncionario):
        f = Funcionario()
        sql_select = f"""
        SELECT {",".join(f.columns())} FROM "Funcionario"
        WHERE "cpfFuncionario" = %s
        """
        # print(sql_select, [cpfFuncionario])
        result = self.db.execute_query(sql_select, [cpfFuncionario], fetch=True)
        if result:
            return Funcionario(*result)
        return None

    def get_all(self):
        f = Funcionario()
        sql_select = f"""
        SELECT {",".join(f.columns())}
        FROM "Funcionario"
        ORDER BY "nome"
        """
        results = self.db.execute_query(sql_select, fetch=True)
        return [Funcionario(*row) for row in results] if results else []
