class Funcionario:
    def __init__(self, cpfFuncionario, sexo, telefone, nome, dataContratacao, cargo):
        self.sexo = sexo
        self.telefone = telefone
        self.nome = nome
        self.dataContratacao = dataContratacao
        self.cargo = cargo
        self.cpfFuncionario = cpfFuncionario

    def to_tuple(self):
        return (
            self.sexo,
            self.telefone,
            self.nome,
            self.dataContratacao,
            self.cargo,
            self.cpfFuncionario,
        )

    def columns(self):
        return [
            '"sexo"',
            '"telefone"',
            '"nome"',
            '"dataContratacao"',
            '"cargo"',
            '"cpfFuncionario"',
        ]
