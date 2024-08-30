from Objetos.Entrada import Entrada
from Integracao.DBOperation import DBOperation


class DBEntrada(DBOperation):

    def create_table(self):
        sql_create = """
        CREATE TABLE "Entrada" (
        "codOperacao" integer PRIMARY KEY DEFAULT nextval('codOperacao_seq'),
        "descricao" varchar,
        "dataLancamento" date NOT NULL,
        "dataConfirmacao" date,
        "status" varchar(10) DEFAULT 'pendente',
        "pendente" bool NOT NULL DEFAULT true,
        "aprovado" bool NOT NULL DEFAULT false,
        "numLote" integer NOT NULL,
        "cpfEstoquista" character(11),
        "cpfOperador" character(11) NOT NULL
        );
        """
        self.db.execute_query(sql_create)

    def insert(self, entrada: Entrada):
        sql_insert = f"""
        INSERT INTO "Entrada" ({",".join(entrada.columns())})
        VALUES ({",".join(["%s"]*len(entrada.columns()))})
        """
        # print(sql_insert)
        self.db.execute_query(sql_insert, entrada.to_tuple())

    def update(self, entrada: Entrada):
        sql_update = f"""
        UPDATE "Entrada" 
        SET {", ".join([f"{c} = %s" for c in entrada.columns()[:-1]])}
        WHERE "codOperacao" = %s
        """
        self.db.execute_query(sql_update, entrada.to_tuple())

    def delete(self, codOperacao):
        sql_delete = """
        DELETE FROM "Entrada"
        WHERE "codOperacao" = %s
        """
        self.db.execute_query(sql_delete, [codOperacao])

    def delete_all(self):
        sql_delete_all = """
        DELETE FROM "Entrada"
        """
        self.db.execute_query(sql_delete_all)

    def get_by_id(self, codOperacao):
        sql_select = """
        SELECT * FROM "Entrada"
        WHERE "codOperacao" = %s
        """
        result = self.db.execute_query(sql_select, [codOperacao], fetch=True)
        if result:
            return Entrada(*result)
        return None

    def get_all(self):
        sql_select = """
        SELECT * FROM "Entrada"
        """
        results = self.db.execute_query(sql_select, fetch=True)
        return [Entrada(*row) for row in results] if results else []
