class Produto:

    def __init__(
        self,
        idProduto=None,
        unidade=None,
        quantidade=None,
        nome=None,
        descricao=None,
        idCategoria=None,
    ):
        self.idProduto = idProduto
        self.unidade = unidade
        self.quantidade = quantidade
        self.nome = nome
        self.descricao = descricao
        self.idCategoria = idCategoria

    def __str__(self):
        return "Produto"

    def to_tuple(self):
        return (
            self.unidade,
            self.quantidade,
            self.nome,
            self.descricao,
            self.idCategoria,
            self.idProduto,
        )

    def columns(self):
        return [
            '"unidade"',
            '"quantidade"',
            '"nome"',
            '"descricao"',
            '"idCategoria"',
            '"idProduto"',
        ]
