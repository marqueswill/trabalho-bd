class Entrada:

    def __init__(
        self,
        codOperacao=None,
        descricao=None,
        dataLancamento=None,
        dataConfirmacao=None,
        status=None,
        pendente=None,
        aprovado=None,
        numLote=None,
        cpfEstoquista=None,
        cpfOperador=None,
        codEstoque=None,
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
            self.pendente,
            self.aprovado,
            self.numLote,
            self.cpfEstoquista,
            self.cpfOperador,
            self.codEstoque,
            self.status,
            self.codOperacao,
        )

    def columns(self):
        return (
            '"descricao"',
            '"dataLancamento"',
            '"dataConfirmacao"',
            '"pendente"',
            '"aprovado"',
            '"numLote"',
            '"cpfEstoquista"',
            '"cpfOperador"',
            '"codEstoque"',
            '"status"',
            '"codOperacao"',
        )
