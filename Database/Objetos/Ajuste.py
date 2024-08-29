class Ajuste:
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
        codProduto,
        codEstoque,
        dataInv,
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
        self.cpfOperador = cpfOperador
        self.codProduto = codProduto
        self.codEstoque = codEstoque
        self.dataInv = dataInv

    def to_tuple(self):
        return (
            self.codOperacao,
            self.descricao,
            self.dataLancamento,
            self.dataConfirmacao,
            self.status,
            self.pendente,
            self.aprovado,
            self.numLote,
            self.cpfEstoquista,
            self.cpfOperador,
            self.codProduto,
            self.codEstoque,
            self.dataInv,
        )
