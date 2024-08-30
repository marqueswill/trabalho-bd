import psycopg2
from psycopg2 import OperationalError
import json


class Database:
    def __init__(self, config_file="dbConfig.json", teste=False):
        self.config_file = config_file
        self.connection = None
        self.load_config(teste)

    def load_config(self, teste):
        if teste:
            index = "test"
        else:
            index = "dev"
        with open(self.config_file, "r") as f:
            config = json.load(f)
            self.database = config[index]["database"]
            self.host = config[index]["host"]
            self.user = config[index]["user"]
            self.password = config[index]["password"]
            self.port = config[index]["port"]

    def create_connection(self):
        try:
            self.connection = psycopg2.connect(
                database=self.database,
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port,
            )
            return self.connection
        except OperationalError as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

    def close_connection(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None
            # print("Conexão ao PostgreSQL finalizada")

    def execute_query(self, query, params=None, fetch=False):
        if self.connection is None:
            self.create_connection()

        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)

            if fetch:
                if cursor.rowcount > 1:  # Se há mais de uma linha, retorna todas
                    return cursor.fetchall()
                elif cursor.rowcount == 1:  # Se há apenas uma linha, retorna uma
                    return cursor.fetchone()
                else:
                    return None
            else:
                self.connection.commit()
                return cursor
        except Exception as e:
            # print(f"Erro ao executar a consulta: {e}")
            # return None
            raise Exception(e)
            # return e
        finally:
            if cursor and not fetch:
                cursor.close()
            if not fetch:
                self.close_connection()
