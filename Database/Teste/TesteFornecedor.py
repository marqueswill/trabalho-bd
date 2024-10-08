from Database.Integracao.DBFornecedor import DBFornecedor
from Database.Objetos.Fornecedor import Fornecedor
from Database.Teste.TesteBase import TesteBase


class TesteFornecedor(TesteBase):
    def __init__(self):
        self.fornecedor_db = DBFornecedor(teste=True)

    def test_insert(self):
        try:
            fornecedores = [
                Fornecedor(
                    endereco="Rua A, 123i",
                    razao="Fornecedor Ain Ltda",
                    nome="Fornecedor Ain",
                    telefone=11987654321,
                    cnpjFornecedor="85920376000145",
                ),
                Fornecedor(
                    endereco="Avenida B, 456",
                    razao="Fornecedor B ME",
                    nome="Fornecedor B",
                    telefone=11912345678,
                    cnpjFornecedor="98765432000188",
                ),
                Fornecedor(
                    endereco="Travessa C, 789",
                    razao="Fornecedor C Comércio",
                    nome="Fornecedor C",
                    telefone=11998765432,
                    cnpjFornecedor="56789012000177",
                ),
            ]
            for f in fornecedores:
                self.fornecedor_db.insert(f)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_get_by_id(self):
        try:
            fornecedor = self.fornecedor_db.get_by_id("85920376000145")

            if fornecedor:
                return "Success"
            else:
                return "Failed - No fornecedor found"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_get_all(self):
        try:
            self.fornecedor_db.get_all()
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"

    def test_update(self):
        try:
            fornecedor = self.fornecedor_db.get_by_id("85920376000145")

            fornecedor.endereco = "Avenida das Flores, 987, Jardim Primavera"
            fornecedor.razao = "Flores & Cia Comércio de Plantas Ltda"
            fornecedor.nome = "Flores & Cia"

            # print(fornecedor.to_tuple())
            self.fornecedor_db.update(fornecedor)

            return "Success"

        except Exception as e:
            return f"Failed - {str(e)}"

    def test_delete(self):
        try:
            f = self.fornecedor_db.get_by_id("56789012000177")
            self.fornecedor_db.delete(f)
            return "Success"
        except Exception as e:
            return f"Failed - {str(e)}"
