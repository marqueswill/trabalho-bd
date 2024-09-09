CREATE OR REPLACE VIEW Cotacao_Produtos AS
    SELECT
        cat."nome" AS categoria_nome,
        p."nome" AS produto_nome,
        p."descricao",
        p."quantidade",
        p."unidade",
        ROUND(AVG(c.valor::numeric), 2) AS preco_medio,
        ROUND(MIN(c.valor::numeric), 2) AS menor_preco,
        ROUND(MAX(c.valor::numeric), 2) AS maior_preco
    FROM
        "Produto" p
    LEFT JOIN "Cotacao" c ON p."codProduto" = c."codProduto"
    INNER JOIN "Categoria" cat ON p."codCategoria" = cat."codCategoria" 
    GROUP BY
        p."codProduto", p."nome", p."descricao", p."quantidade", p."unidade", cat."nome"
    ORDER BY
        cat."nome",p."nome" ASC;

CREATE VIEW View_Produtos_Fornecedores AS
    SELECT 
        p."nome" AS produto,
        f."nome" AS fornecedor,
        c."valor" AS valorCotacao
    FROM 
        "Cotacao" c
    JOIN 
        "Fornecedor" f ON c."cnpjFornecedor" = f."cnpjFornecedor"
    JOIN 
        "Produto" p ON c."codProduto" = p."codProduto";

-- transformar em procedure que retornar as operações para o estoque escolhido
CREATE VIEW Operacoes_Estoque AS
    SELECT 
        'Entrada' AS "tipo_operacao",
        "codOperacao",
        "descricao",
        "dataLancamento",
        "status",
        "dataConfirmacao"
        -- "pendente",
        -- "aprovado",
        -- "numLote",
        -- "cpfEstoquista",
        -- "cpfOperador"
    FROM "Entrada"

    UNION ALL

    SELECT 
        'Saida' AS "tipo_operacao",
        "codOperacao",
        "descricao",
        "dataLancamento",
        "status",
        "dataConfirmacao"
        -- "pendente",
        -- "aprovado",
        -- "numLote",
        -- "cpfEstoquista",
        -- "cpfOperador"
    FROM "Saida"
    WHERE "codEstoque" = 1
    ORDER BY "status" DESC, "dataLancamento" ASC;
