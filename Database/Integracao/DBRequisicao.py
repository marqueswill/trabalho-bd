from Objetos.Requisicao import Requisicao
from Integracao.DBOperation import DBOperation


class DBRequisicao(DBOperation):

    def create_table(self):
        sql_create = """
        CREATE TABLE "Requisicao" (
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

    def insert(self, requisicao: Requisicao):
        sql_insert = f"""
        INSERT INTO "Requisicao" ({",".join(requisicao.columns())})
        VALUES ({",".join(["%s"]*len(requisicao.columns()))})
        """
        # print(sql_insert)
        self.db.execute_query(sql_insert, requisicao.to_tuple())

    def update(self, requisicao: Requisicao):
        sql_update = f"""
        UPDATE "Requisicao" 
        SET {", ".join([f"{c} = %s" for c in requisicao.columns() if c != "codOperacao"])}
        WHERE "codOperacao" = %s
        """
        self.db.execute_query(sql_update, requisicao.to_tuple())

    def delete(self, codOperacao):
        sql_delete = """
        DELETE FROM "Requisicao"
        WHERE "codOperacao" = %s
        """
        self.db.execute_query(sql_delete, [codOperacao])

    def delete_all(self):
        sql_delete_all = """
        DELETE FROM "Requisicao"
        """
        self.db.execute_query(sql_delete_all)

    def get_by_id(self, codOperacao):
        sql_select = """
        SELECT * FROM "Requisicao"
        WHERE "codOperacao" = %s
        """
        result = self.db.execute_query(sql_select, [codOperacao], fetch=True)
        if result:
            return Requisicao(*result)
        return None

    def get_all(self):
        sql_select = """
        SELECT * FROM "Requisicao"
        """
        results = self.db.execute_query(sql_select, fetch=True)
        return [Requisicao(*row) for row in results] if results else []
