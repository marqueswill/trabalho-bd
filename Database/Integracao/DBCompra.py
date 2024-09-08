from Database.Objetos.Compra import Compra
from Database.Integracao.DBOperation import DBOperation


class DBCompra(DBOperation):
    def __init__(self, teste=False):
        super().__init__(teste)

    def get_as_bytea(self, pdf_path):
        try:
            with open(pdf_path, "rb") as file:
                return file.read()
        except Exception as e:
            print(f"Erro ao ler o arquivo PDF: {e}")
            return None

    def insert(self, compra: Compra):
        sql_insert = f"""
        INSERT INTO "Compra" ({",".join(compra.columns())})
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        self.db.execute_query(sql_insert, compra.to_tuple())

    def update(self, compra: Compra):
        sql_update = """
        UPDATE "Compra" 
        SET "data" = %s, "notaFiscal" = %s
        WHERE "numNF" = %s
        """
        params = [compra.data, compra.notaFiscal, compra.numNF]
        self.db.execute_query(sql_update, params)

    def delete(self, compra: Compra):
        sql_delete = """
        DELETE FROM "Compra"
        WHERE "numNF" = %s
        """
        self.db.execute_query(sql_delete, [compra.numNF])

    def get_by_id(self, numNF):
        c = Compra()
        sql_select = f"""
        SELECT {",".join(c.columns())} 
        FROM "Compra"
        WHERE "numNF" = %s
        """
        result = self.db.execute_query(sql_select, [numNF], fetch=True)
        if result:
            return Compra(*result)
        return None

    def get_all(self):
        c = Compra()
        sql_select = f"""
        SELECT {",".join(c.columns())} 
        FROM "Compra"
        """
        results = self.db.execute_query(sql_select, fetch=True)
        return [Compra(*row) for row in results] if results else []
