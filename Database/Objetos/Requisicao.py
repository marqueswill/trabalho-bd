class Requisicao:
    def __init__(
        self,
        codOperacao=0,
        descricao="",
        dataLancamento="",
        dataConfirmacao="",
        status="",
        pendente=True,
        aprovado=False,
        numLote=0,
        cpfEstoquista="",
        cpfOperador="",
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
            '"codOperacao"',
        )
