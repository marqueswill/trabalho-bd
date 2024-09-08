from Database.Teste.TesteBase import TesteBase

from Database.Integracao.DBFuncionario import DBFuncionario
from Database.Objetos.Funcionario import Funcionario


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
                    cnpjRestaurante="87654321000188",
                ),
                Funcionario(
                    cpfFuncionario="09876543211",
                    sexo="F",
                    telefone=1987654321,
                    nome="Jane Smith",
                    dataContratacao="2024-02-15",
                    cargo="O",
                    cnpjRestaurante="87654321000188",
                ),
                Funcionario(
                    cpfFuncionario="12345678999",
                    sexo="M",
                    telefone=198765151,
                    nome="João Pedro",
                    dataContratacao="2023-02-15",
                    cargo="E",
                    cnpjRestaurante="87654321000188",
                ),
            ]

            for f in funcionarios:
                self.funcionario_db.insert(f)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_get_by_id(self):
        try:
            funcionario = self.funcionario_db.get_by_id("12345678900")

            if funcionario:
                return "Success"
            else:
                return "Failed - No funcionario found"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_get_all(self):
        try:
            self.funcionario_db.get_all()
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_update(self):
        try:
            funcionario = self.funcionario_db.get_by_id("12345678999")
            funcionario.nome = "Lohane Vekanandre Smith Bueno"
            funcionario.sexo = "F"

            self.funcionario_db.update(funcionario)

            return "Success"

        except Exception as e:
            return f"Failed - {str(e)}"

    def test_delete(self):
        try:
            f = self.funcionario_db.get_by_id("12345678900")
            self.funcionario_db.delete(f)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
