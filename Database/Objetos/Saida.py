class Saida:

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
        codRequisicao,
    ):
        self.descricao = descricao
        self.dataLancamento = dataLancamento
        self.dataConfirmacao = dataConfirmacao
        self.status = status
        self.pendente = pendente
        self.aprovado = aprovado
        self.numLote = numLote
        self.cpfEstoquista = cpfEstoquista
        self.cpfOperador = cpfOperador
        self.codRequisicao = codRequisicao
        self.codEstoque = codEstoque
        self.codOperacao = codOperacao

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
            self.codRequisicao,
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
            '"codRequisicao"',
            '"codEstoque"',
            '"codOperacao"',
        )
