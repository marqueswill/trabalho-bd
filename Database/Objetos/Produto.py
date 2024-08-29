class Produto:
    def __init__(self, idProduto, unidade, quantidade, descricao, idCategoria, nome):
        self.idProduto = idProduto
        self.unidade = unidade
        self.quantidade = quantidade
        self.descricao = descricao
        self.idCategoria = idCategoria
        self.nome = nome

    def to_tuple(self):
        return (
            self.idProduto,
            self.unidade,
            self.quantidade,
            self.descricao,
            self.idCategoria,
            self.nome,
        )
