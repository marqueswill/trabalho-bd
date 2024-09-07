class Saida:

    def __init__(
        self,
        codOperacao=None,
        descricao=None,
        dataLancamento=None,
        dataConfirmacao=None,
        status="pendente",
        pendente=True,
        aprovado=False,
        numLote=None,
        cpfEstoquista=None,
        cpfOperador=None,
        codEstoque=None,
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
        self.codEstoque = codEstoque
        self.codOperacao = codOperacao

    def __str__(self):
        return "Saida"

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
