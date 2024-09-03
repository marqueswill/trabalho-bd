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

        -- Inserir as operações de Requisicao
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

        -- Inserir as operações de Saida
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

        -- Os resultados estão agora na tabela "historico_operacoes".
        -- Essa tabela pode ser consultada após a execução da procedure.
        -- Caso você queira transferir esses dados para uma tabela permanente:
        -- INSERT INTO historico_operacoes_estq (tipo_operacao, codOperacao, descricao, dataLancamento, etc.)
        -- SELECT * FROM "historico_operacoes";

        -- Não é necessário um retorno aqui, pois é uma PROCEDURE.

    END;
$$;


-- CREATE OR REPLACE PROCEDURE trocar_estoque(
--     estoque_origem INTEGER,
--     produtos INTEGER[],
--     qunatidades INTEGER[],
--     estoque_destino INTEGER
-- )
-- LANGUAGE plpgsql
-- AS $$
-- DECLARE
--     produto INTEGER;
--     quantidade INTEGER;
-- BEGIN
--     -- Loop através da lista de produtos
--     FOREACH produto IN ARRAY produtos
--     LOOP
--         -- Verifica se o produto existe no estoque de origem
--         SELECT "estoqueAtual" INTO quantidade
--         FROM "ProdutoEstoque"
--         WHERE "codProduto" = produto
--           AND "codEstoque" = estoque_origem;

--         IF FOUND THEN
--             -- Verifica se há estoque suficiente
--             IF quantidade > 0 THEN
--                 -- Atualiza o estoque no estoque de origem
--                 UPDATE "ProdutoEstoque"
--                 SET "estoqueAtual" = "estoqueAtual" - 1
--                 WHERE "codProduto" = produto
--                   AND "codEstoque" = estoque_origem;

--                 -- Atualiza o estoque no estoque de destino
--                 -- Verifica se o produto já existe no estoque de destino
--                 IF EXISTS (
--                     SELECT 1
--                     FROM "ProdutoEstoque"
--                     WHERE "codProduto" = produto
--                       AND "codEstoque" = estoque_destino
--                 ) THEN
--                     UPDATE "ProdutoEstoque"
--                     SET "estoqueAtual" = "estoqueAtual" + 1
--                     WHERE "codProduto" = produto
--                       AND "codEstoque" = estoque_destino;
--                 ELSE
--                     INSERT INTO "ProdutoEstoque" ("codProduto", "codEstoque", "estoqueAtual", "estoqueMax", "estoqueMin", "estoqueDisp", "ultimoInv")
--                     VALUES (produto, estoque_destino, 1, 0, 0, 0, NULL);
--                 END IF;
--             ELSE
--                 RAISE NOTICE 'Produto % não tem estoque suficiente no estoque de origem.', produto;
--             END IF;
--         ELSE
--             RAISE NOTICE 'Produto % não encontrado no estoque de origem.', produto;
--         END IF;
--     END LOOP;
-- END;
-- $$;

-- Primeiro, defina o tipo composto para a lista de tuplas
DROP TYPE IF EXISTS produto_quantidade CASCADE;
CREATE TYPE produto_quantidade AS (
    codProduto INTEGER,
    quantidade INTEGER
);

-- Atualize a procedure para usar o tipo composto
CREATE OR REPLACE PROCEDURE trocar_estoque(
    estoque_origem INTEGER,
    produtos_quantidades produto_quantidade[],
    estoque_destino INTEGER
)
LANGUAGE plpgsql
AS $$
DECLARE
    item produto_quantidade;
    estoque_atual INTEGER;
BEGIN
    -- Loop através da lista de produtos e quantidades
    FOREACH item IN ARRAY produtos_quantidades
    LOOP
        -- Verifica se o produto existe no estoque de origem
        SELECT "estoqueAtual" INTO estoque_atual
        FROM "ProdutoEstoque"
        WHERE "codProduto" = item.codProduto
          AND "codEstoque" = estoque_origem;

        IF FOUND THEN
            -- Verifica se há estoque suficiente
            IF estoque_atual >= item.quantidade THEN
                -- Atualiza o estoque no estoque de origem
                UPDATE "ProdutoEstoque"
                SET "estoqueAtual" = "estoqueAtual" - item.quantidade
                WHERE "codProduto" = item.codProduto
                  AND "codEstoque" = estoque_origem;

                -- Atualiza o estoque no estoque de destino
                -- Verifica se o produto já existe no estoque de destino
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
