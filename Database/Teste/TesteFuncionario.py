from Teste.TesteLote import TesteLote
from Teste.TesteBase import TesteBase


from Integracao.DBFuncionario import DBFuncionario
from Objetos.Funcionario import Funcionario


class TesteFuncionario(TesteBase):
    def __init__(self):
        self.funcionario_db = DBFuncionario(teste=True)

    def test_insert(self):
        try:

            funcionarios = [
                Funcionario(
                    cpfFuncionario="12345678900",
                    sexo="M",
                    telefone=1234567890,
                    nome="John Doe",
                    dataContratacao="2024-01-01",
                    cargo="G",
                ),
                Funcionario(
                    cpfFuncionario="09876543211",
                    sexo="F",
                    telefone=1987654321,
                    nome="Jane Smith",
                    dataContratacao="2024-02-15",
                    cargo="O",
                ),
                Funcionario(
                    cpfFuncionario="12345678999",
                    sexo="M",
                    telefone=198765151,
                    nome="João Pedro",
                    dataContratacao="2023-02-15",
                    cargo="E",
                ),
            ]

            for f in funcionarios:
                self.funcionario_db.insert(f)
            return "test_insert: Success"
        except Exception as e:
            return f"test_insert: Failed - {str(e)}"

    def test_get_by_id(self):
        try:
            funcionario = self.funcionario_db.get_by_id("12345678900")
            if funcionario:
                return "test_get_by_id: Success"
            else:
                return "test_get_by_id: Failed - No funcionario found"
        except Exception as e:
            return f"test_get_by_id: Failed - {str(e)}"

    def test_get_all(self):
        try:
            self.funcionario_db.get_all()
            return "test_get_all: Success"
        except Exception as e:
            return f"test_get_all: Failed - {str(e)}"

    def test_delete(self):
        try:
            self.funcionario_db.delete("02345678900")
            return "test_delete: Success"
        except Exception as e:
            return f"test_delete: Failed - {str(e)}"

    def test_delete_all(self):
        try:
            self.funcionario_db.delete_all()
            return "delete_all: Success"
        except Exception as e:
            return f"delete_all: Failed - {str(e)}"
