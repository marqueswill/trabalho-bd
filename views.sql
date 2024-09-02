CREATE OR REPLACE VIEW Cotacao_Produtos AS
    SELECT
        p."codProduto",
        p."nome",
        p."descricao",
        p."quantidade",
        p."unidade",
        p."codCategoria",
        ROUND(AVG(c.valor::numeric), 2) AS preco_medio,
        ROUND(MIN(c.valor::numeric), 2) AS menor_preco,
        ROUND(MAX(c.valor::numeric), 2) AS maior_preco
    FROM
        "Produto" p
    LEFT JOIN
        "Cotacao" c
    ON
        p."codProduto" = c."codProduto"
    GROUP BY
        p."codProduto", p."nome", p."descricao", p."quantidade", p."unidade", p."codCategoria"
    ORDER BY
        "codProduto" ASC;


CREATE VIEW View_Produtos_Fornecedores AS
    SELECT 
        f."nome" AS fornecedor,
        f."razao",
        p."nome" AS produto,
        c."valor" AS valorCotacao
    FROM 
        "Cotacao" c
    JOIN 
        "Fornecedor" f ON c."cnpjFornecedor" = f."cnpjFornecedor"
    JOIN 
        "Produto" p ON c."codProduto" = p."codProduto";

-- CREATE VIEW Operacoes_Estoque AS
--     SELECT 
--         'Entrada' AS "tipo_operacao",
--         "codOperacao",
--         "descricao",
--         "dataLancamento",
--         "dataConfirmacao",
--         "status",
--         "pendente",
--         "aprovado",
--         "numLote",
--         "cpfEstoquista",
--         "cpfOperador"
--     FROM "Entrada"

--     UNION ALL

--     SELECT 
--         'Requisicao' AS "tipo_operacao",
--         "codOperacao",
--         "descricao",
--         "dataLancamento",
--         "dataConfirmacao",
--         "status",
--         "pendente",
--         "aprovado",
--         "numLote",
--         "cpfEstoquista",
--         "cpfOperador"
--     FROM "Requisicao"

--     UNION ALL

--     SELECT 
--         'Saida' AS "tipo_operacao",
--         "codOperacao",
--         "descricao",
--         "dataLancamento",
--         "dataConfirmacao",
--         "status",
--         "pendente",
--         "aprovado",
--         "numLote",
--         "cpfEstoquista",
--         "cpfOperador"
--     FROM "Saida"

--     ORDER BY "dataLancamento";
