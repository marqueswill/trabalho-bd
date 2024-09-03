class Entrada:

    def __init__(
        self,
        codOperacao,
        descricao,
        dataLancamento,
        dataConfirmacao,
        status,
        pendente,
        aprovado,
        numLote,
        cpfEstoquista,
        cpfOperador,
        codEstoque,
    ):
        self.codOperacao = codOperacao
        self.descricao = descricao
        self.dataLancamento = dataLancamento
        self.dataConfirmacao = dataConfirmacao
        self.status = status
        self.pendente = pendente
        self.aprovado = aprovado
        self.numLote = numLote
        self.cpfEstoquista = cpfEstoquista
        self.codEstoque = codEstoque
        self.cpfOperador = cpfOperador

    def to_tuple(self):
        return (
            self.descricao,
            self.dataLancamento,
            self.dataConfirmacao,
            self.status,
            self.pendente,
            self.aprovado,
            self.numLote,
            self.cpfEstoquista,
            self.cpfOperador,
            self.codEstoque,
            self.codOperacao,
        )

    def columns(self):
        return (
            '"descricao"',
            '"dataLancamento"',
            '"dataConfirmacao"',
            '"status"',
            '"pendente"',
            '"aprovado"',
            '"numLote"',
            '"cpfEstoquista"',
            '"cpfOperador"',
            '"codEstoque"',
            '"codOperacao"',
        )
