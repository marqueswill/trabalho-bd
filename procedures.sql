CREATE OR REPLACE PROCEDURE Gerar_Historico_Operacoes_Estoque(p_codEstoque integer)
LANGUAGE plpgsql 
AS $$
    BEGIN
        DROP TABLE IF EXISTS "historico_operacoes";

        -- Criar tabela temporária para armazenar o resultado
        CREATE TEMP TABLE "historico_operacoes" (
            "tipo_operacao" TEXT,
            "codOperacao" INT,
            "descricao" TEXT,
            "dataLancamento" TIMESTAMP,
            "dataConfirmacao" TIMESTAMP,
            "status" TEXT,
            "pendente" BOOLEAN,
            "aprovado" BOOLEAN,
            "numLote" INT,
            "cpfEstoquista" VARCHAR,
            "cpfOperador" VARCHAR
        );

        -- Inserir as operações de Entrada
        INSERT INTO "historico_operacoes"
        SELECT 
            'Entrada' AS tipo_operacao,
            e."codOperacao",
            e."descricao",
            e."dataLancamento",
            e."dataConfirmacao",
            e."status",
            e."pendente",
            e."aprovado",
            e."numLote",
            e."cpfEstoquista",
            e."cpfOperador"
        FROM "Entrada" e
        WHERE e."codEstoque" = p_codEstoque;

        INSERT INTO "historico_operacoes"
        SELECT 
            'Requisicao' AS tipo_operacao,
            r."codOperacao",
            r."descricao",
            r."dataLancamento",
            r."dataConfirmacao",
            r."status",
            r."pendente",
            r."aprovado",
            r."numLote",
            r."cpfEstoquista",
            r."cpfOperador"
        FROM "Requisicao" r
        WHERE r."codEstoque" = p_codEstoque;

        INSERT INTO "historico_operacoes"
        SELECT 
            'Saida' AS tipo_operacao,
            s."codOperacao",
            s."descricao",
            s."dataLancamento",
            s."dataConfirmacao",
            s."status",
            s."pendente",
            s."aprovado",
            s."numLote",
            s."cpfEstoquista",
            s."cpfOperador"
        FROM "Saida" s
        WHERE s."codEstoque" = p_codEstoque;

    END;
$$;

DROP TYPE IF EXISTS produto_quantidade CASCADE;

CREATE TYPE produto_quantidade AS (
    codProduto INTEGER,
    quantidade INTEGER
);

CREATE OR REPLACE PROCEDURE trocar_estoque(
    estoque_origem INTEGER,
    estoque_destino INTEGER,
    produtos_quantidades produto_quantidade[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    item produto_quantidade;
    estoque_atual INTEGER;
BEGIN
    FOREACH item IN ARRAY produtos_quantidades
    LOOP
        SELECT "estoqueAtual" INTO estoque_atual
        FROM "ProdutoEstoque"
        WHERE "codProduto" = item.codProduto
          AND "codEstoque" = estoque_origem;

        IF FOUND THEN
            IF estoque_atual >= item.quantidade THEN
                UPDATE "Saida" s
                SET "pendente" = false, "aprovado" = false
                FROM "Lote" l
                JOIN "ProdutoLote" pl ON pl."numLote" = l."numLote"
                WHERE s."pendente" = true
                AND s."numLote" = l."numLote"
                AND s."codEstoque" = estoque_origem
                AND pl."codProduto" = item.codProduto;

                UPDATE "ProdutoEstoque"
                SET "estoqueAtual" = "estoqueAtual" - item.quantidade,
                    "estoqueDisp" = "estoqueDisp" - item.quantidade
                WHERE "codProduto" = item.codProduto
                  AND "codEstoque" = estoque_origem;


                IF EXISTS (
                    SELECT 1
                    FROM "ProdutoEstoque"
                    WHERE "codProduto" = item.codProduto
                      AND "codEstoque" = estoque_destino
                ) THEN
                    UPDATE "ProdutoEstoque"
                    SET "estoqueAtual" = "estoqueAtual" + item.quantidade,
                        "estoqueDisp" = "estoqueDisp" + item.quantidade
                    WHERE "codProduto" = item.codProduto
                      AND "codEstoque" = estoque_destino;
                ELSE
                    INSERT INTO "ProdutoEstoque" ("codProduto", "codEstoque", "estoqueAtual", "estoqueMax", "estoqueMin", "estoqueDisp", "ultimoInv")
                    VALUES (item.codProduto, estoque_destino, item.quantidade, 0, 0, item.quantidade, NULL);
                END IF;
            ELSE
                RAISE NOTICE 'Produto % não tem estoque suficiente no estoque de origem.', item.codProduto;
            END IF;
        ELSE
            RAISE NOTICE 'Produto % não encontrado no estoque de origem.', item.codProduto;
        END IF;
    END LOOP;
END;
$$;

---- EXEMPLO:
-- CALL trocar_estoque(
--     1,
-- 	5,
--     ARRAY[
--         (1, 10)::produto_quantidade, 
--         (2, 10)::produto_quantidade   
--     ]
-- );

-- SELECT * FROM "ProdutoEstoque" ORDER BY "codEstoque", "codProduto";

