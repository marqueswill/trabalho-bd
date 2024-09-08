class Funcionario:

    def __init__(
        self,
        sexo=None,
        telefone=None,
        nome=None,
        dataContratacao=None,
        cargo=None,
        cnpjRestaurante=None,
        cpfFuncionario=None,
    ):
        self.sexo = sexo
        self.telefone = telefone
        self.nome = nome
        self.dataContratacao = dataContratacao
        self.cargo = cargo
        self.cnpjRestaurante = cnpjRestaurante
        self.cpfFuncionario = cpfFuncionario

    def __str__(self):
        return "Funcionario"

    def to_tuple(self):
        return (
            self.sexo,
            self.telefone,
            self.nome,
            self.dataContratacao,
            self.cargo,
            self.cnpjRestaurante,
            self.cpfFuncionario,
        )

    def columns(self):
        return [
            '"sexo"',
            '"telefone"',
            '"nome"',
            '"dataContratacao"',
            '"cargo"',
            '"cnpjRestaurante"',
            '"cpfFuncionario"',
        ]

    def auto_columns(self):
        return []

    def keys(self):
        return [
            '"cpfFuncionario"',
        ]
