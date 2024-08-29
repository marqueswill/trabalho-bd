class Funcionario:
    def __init__(self, cpfFuncionario, sexo, telefone, nome, dataContratacao, cargo):
        self.cpfFuncionario = cpfFuncionario
        self.sexo = sexo
        self.telefone = telefone
        self.nome = nome
        self.dataContratacao = dataContratacao
        self.cargo = cargo

    def to_tuple(self):
        return (
            self.cpfFuncionario,
            self.sexo,
            self.telefone,
            self.nome,
            self.dataContratacao,
            self.cargo,
        )
