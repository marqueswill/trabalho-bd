from Objetos.Saida import Saida
from Integracao.DBOperation import DBOperation


class DBSaida(DBOperation):
    def __init__(self, teste=False):
        super().__init__(teste)
        
    def create_table(self):
        sql_create = """
        CREATE TABLE "Saida" (
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
        "codRequisicao" integer NOT NULL
        );
        """
        self.db.execute_query(sql_create)

    def insert(self, saida: Saida):
        sql_insert = f"""
        INSERT INTO "Saida" ({",".join(saida.columns())})
        VALUES ({",".join(["%s"]*len(saida.columns()))})
        """
        # print(sql_insert)
        self.db.execute_query(sql_insert, saida.to_tuple())

    def update(self, saida: Saida):
        sql_update = f"""
        UPDATE "Saida" 
        SET {", ".join([f"{c} = %s" for c in saida.columns() if c != "codOperacao"])}
        WHERE "codOperacao" = %s
        """
        self.db.execute_query(sql_update, saida.to_tuple())

    def delete(self, codOperacao):
        sql_delete = """
        DELETE FROM "Saida"
        WHERE "codOperacao" = %s
        """
        self.db.execute_query(sql_delete, [codOperacao])

    def delete_all(self):
        sql_delete_all = """
        DELETE FROM "Saida"
        """
        self.db.execute_query(sql_delete_all)

    def get_by_id(self, codOperacao):
        sql_select = """
        SELECT * FROM "Saida"
        WHERE "codOperacao" = %s
        """
        result = self.db.execute_query(sql_select, [codOperacao], fetch=True)
        if result:
            return Saida(*result)
        return None

    def get_all(self):
        sql_select = """
        SELECT * FROM "Saida"
        """
        results = self.db.execute_query(sql_select, fetch=True)
        return [Saida(*row) for row in results] if results else []
