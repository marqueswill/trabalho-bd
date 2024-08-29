from Objetos.Ajuste import Ajuste
from Integracao.DBOperation import DBOperation


class DBAjuste(DBOperation):

    def create_table(self):
        sql_create = """
        CREATE TABLE "Ajuste" (
        "codOperacao" integer PRIMARY KEY DEFAULT nextval('codOperacao_seq'),
        "descricao" varchar,
        "dataLancamento" date NOT NULL,
        "dataConfirmacao" date,
        "status" varchar(10) DEFAULT 'pendente',
        "pendente" bool NOT NULL DEFAULT true,
        "aprovado" bool NOT NULL DEFAULT false,
        "numLote" integer NOT NULL,
        "cpfEstoquista" character(11),
        "cpfOperador" character(11) NOT NULL,
        "codProduto" integer NOT NULL,
        "codEstoque" integer NOT NULL,
        "dataInv" date NOT NULL
        );
        """
        self.db.execute_query(sql_create)

    def insert(self, ajuste: Ajuste):
        sql_insert = f"""
        INSERT INTO "Ajuste" ({",".join(ajuste.columns())})
        VALUES ({",".join(["%s"]*len(ajuste.columns()))})
        """
        # print(sql_insert)
        self.db.execute_query(sql_insert, ajuste.to_tuple())

    def update(self, ajuste: Ajuste):
        sql_update = f"""
        UPDATE "Ajuste" 
        SET {", ".join([f"{c} = %s" for c in ajuste.columns() if c != "codOperacao"])}
        WHERE "codOperacao" = %s
        """
        self.db.execute_query(sql_update, ajuste.to_tuple())

    def delete(self, codOperacao):
        sql_delete = """
        DELETE FROM "Ajuste"
        WHERE "codOperacao" = %s
        """
        self.db.execute_query(sql_delete, [codOperacao])

    def delete_all(self):
        sql_delete_all = """
        DELETE FROM "Ajuste"
        """
        self.db.execute_query(sql_delete_all)

    def get_by_id(self, codOperacao):
        sql_select = """
        SELECT * FROM "Ajuste"
        WHERE "codOperacao" = %s
        """
        result = self.db.execute_query(sql_select, [codOperacao], fetch=True)
        if result:
            return Ajuste(*result)
        return None

    def get_all(self):
        sql_select = """
        SELECT * FROM "Ajuste"
        """
        results = self.db.execute_query(sql_select, fetch=True)
        return [Ajuste(*row) for row in results] if results else []
