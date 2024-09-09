-- PROCEDURES 

SELECT * FROM "ProdutoEstoque"
WHERE "codEstoque" = 1 OR "codEstoque" =  5;

SELECT s."codOperacao",s."descricao",s."numLote", p."codProduto",p."nome", pl."quantidade"
FROM "Saida" s
RIGHT JOIN "Lote" l ON l."numLote" = s."numLote"
RIGHT JOIN "ProdutoLote" pl ON pl."numLote" = l."numLote"
LEFT JOIN "Produto" p ON p."codProduto" = pl."codProduto";

SELECT * FROM "ProdutoEstoque";

CALL trocar_estoque(
    1,
	5,
    ARRAY[
        (1, 10)::produto_quantidade, 
        (2, 10)::produto_quantidade   
    ]
);

SELECT * FROM "ProdutoEstoque"
ORDER BY "codEstoque" ASC, "codProduto" ASC;


-- VIEWS
SELECT * FROM operacoes_estoque;
SELECT * FROM view_produtos_fornecedores;
SELECT * FROM cotacao_produtos;