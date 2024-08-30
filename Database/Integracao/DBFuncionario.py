from Objetos.Funcionario import Funcionario
from Integracao.DBOperation import DBOperation


class DBFuncionario(DBOperation):
    def __init__(self, teste=False):
        super().__init__(teste)

    def create_table(self):
        sql_create = """
        CREATE TABLE "Funcionario" (
        "cpfFuncionario" char(11) PRIMARY KEY,
        "sexo" char(1),
        "telefone" bigint,
        "nome" varchar NOT NULL,
        "dataContratacao" date NOT NULL,
        "cargo" char(1) NOT NULL
        );
        """
        self.db.execute_query(sql_create)

    def insert(self, funcionario: Funcionario):
        sql_insert = f"""
        INSERT INTO "Funcionario" ({",".join(funcionario.columns())})
        VALUES ({",".join(["%s"]*len(funcionario.columns()))})
        """
        # print(sql_insert)
        self.db.execute_query(sql_insert, funcionario.to_tuple())

    def update(self, funcionario: Funcionario):
        sql_update = f"""
        UPDATE "Funcionario" 
        SET {", ".join([f"{c} = %s" for c in funcionario.columns() if c != "cpfFuncionario"])}
        WHERE "cpfFuncionario" = %s
        """
        self.db.execute_query(sql_update, funcionario.to_tuple())

    def delete(self, cpfFuncionario):
        sql_delete = """
        DELETE FROM "Funcionario"
        WHERE "cpfFuncionario" = %s
        """
        self.db.execute_query(sql_delete, [cpfFuncionario])

    def delete_all(self):
        sql_delete_all = """
        DELETE FROM "Funcionario"
        """
        self.db.execute_query(sql_delete_all)

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
        SELECT
            "sexo",
            "telefone",
            "nome",
            "dataContratacao",
            "cargo",
            "cpfFuncionario"
        FROM "Funcionario"
        """
        results = self.db.execute_query(sql_select, fetch=True)
        return [Funcionario(*row) for row in results] if results else []
