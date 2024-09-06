class Produto:

    def __init__(
        self,
        idProduto=None,
        unidade=None,
        quantidade=None,
        descricao=None,
        idCategoria=None,
        nome=None,
    ):
        self.idProduto = idProduto
        self.unidade = unidade
        self.quantidade = quantidade
        self.descricao = descricao
        self.idCategoria = idCategoria
        self.nome = nome

    def __str__(self):
        return "Produto"

    def to_tuple(self):
        return (
            self.idProduto,
            self.unidade,
            self.quantidade,
            self.descricao,
            self.idCategoria,
            self.nome,
        )

    def columns(self):
        return [
            "'idProduto'",
            "'unidade'",
            "'quantidade'",
            "'descricao'",
            "'idCategoria'",
            "'nome'",
        ]
