CREATE OR REPLACE VIEW CotacaoProduto AS
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

CREATE VIEW OperacoesEstoque AS
SELECT 
    'Entrada' AS "tipo_operacao",
    "codOperacao",
    "descricao",
    "dataLancamento",
    "dataConfirmacao",
    "status",
    "pendente",
    "aprovado",
    "numLote",
    "cpfEstoquista",
    "cpfOperador"
    -- NULL::integer AS "codRequisicao"  -- Explicitly cast NULL to integer
FROM "Entrada"

UNION ALL

SELECT 
    'Requisicao' AS "tipo_operacao",
    "codOperacao",
    "descricao",
    "dataLancamento",
    "dataConfirmacao",
    "status",
    "pendente",
    "aprovado",
    "numLote",
    "cpfEstoquista",
    "cpfOperador"
    -- NULL::integer AS "codRequisicao"  -- Explicitly cast NULL to integer
FROM "Requisicao"

UNION ALL

SELECT 
    'Saida' AS "tipo_operacao",
    "codOperacao",
    "descricao",
    "dataLancamento",
    "dataConfirmacao",
    "status",
    "pendente",
    "aprovado",
    "numLote",
    "cpfEstoquista",
    "cpfOperador"
    -- "codRequisicao"  -- No need to cast, already integer
FROM "Saida"

ORDER BY "dataLancamento";
