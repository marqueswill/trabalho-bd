import psycopg2
from psycopg2 import OperationalError
import json


class Database:
    def __init__(self, config_file="dbConfig.json"):
        self.config_file = config_file
        self.connection = None
        self.load_config()

    def load_config(self):
        with open(self.config_file, "r") as f:
            config = json.load(f)
            self.database = config["database"]
            self.host = config["host"]
            self.user = config["user"]
            self.password = config["password"]
            self.port = config["port"]

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
            print("Conexão ao PostgreSQL finalizada")

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
            print(f"Erro ao executar a consulta: {e}")
            return None
        finally:
            if cursor and not fetch:
                cursor.close()
            if not fetch:
                self.close_connection()
    
