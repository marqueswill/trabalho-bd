-- FUNCOES
CREATE OR REPLACE FUNCTION atualizar_estoque_entrada()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW."pendente" = true THEN --pendente
        RETURN NEW;
    END IF;

    IF NEW."pendente" = false AND NEW."aprovado" = true THEN --aprovado
        IF NEW."status" = 'aprovado' THEN
            RETURN NEW;
        END IF;

        UPDATE "ProdutoEstoque" pe
        SET "estoqueAtual" = "estoqueAtual" + pl."quantidade",
            "estoqueDisp" = "estoqueDisp" + pl."quantidade"
        FROM "ProdutoLote" pl
        WHERE pe."codProduto" = pl."codProduto"
            AND pe."codEstoque" = pl."codEstoque"
            AND pl."numLote" = NEW."numLote";

        UPDATE "Entrada"
        SET "status" = 'aprovado', "dataConfirmacao" = NOW()
        WHERE "codOperacao" = NEW."codOperacao";

        RETURN NEW;
    END IF;

    IF NEW."pendente" = false AND NEW."aprovado" = false THEN --rejeitado
        IF NEW."status" = 'rejeitado' THEN
            RETURN NEW;
        END IF;

        UPDATE "Entrada"
        SET "status" = 'rejeitado', "dataConfirmacao" = NOW()
        WHERE "codOperacao" = NEW."codOperacao";
        RETURN NEW;
    END IF;

END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION atualizar_estoque_saida()
    RETURNS TRIGGER AS $$
    BEGIN
        
        IF NEW."pendente" = true THEN --pendente
            IF NEW."status" = 'pendente' THEN
                RETURN NEW;
            END IF;

            UPDATE "ProdutoEstoque" pe
            SET "estoqueDisp" = "estoqueDisp" - pl."quantidade"
            FROM "ProdutoLote" pl
            WHERE pe."codProduto" = pl."codProduto"
                AND pe."codEstoque" = pl."codEstoque"
                AND pl."numLote" = NEW."numLote";

            UPDATE "Saida"
            SET "status" = 'pendente'
            WHERE "codOperacao" = NEW."codOperacao";
            RETURN NEW;
        END IF;

        IF NEW."pendente" = false AND NEW."aprovado" = true THEN --aprovado
            IF NEW."status" = 'aprovado' THEN
                RETURN NEW;
            END IF;

            UPDATE "ProdutoEstoque" pe
            SET "estoqueAtual" = "estoqueAtual" - pl."quantidade"
            FROM "ProdutoLote" pl
            WHERE pe."codProduto" = pl."codProduto"
                AND pe."codEstoque" = pl."codEstoque"
                AND pl."numLote" = NEW."numLote";

            UPDATE "Saida"
            SET "status" = 'aprovado', "dataConfirmacao" = NOW()
            WHERE "codOperacao" = NEW."codOperacao";
            RETURN NEW;
        END IF;

        IF NEW."pendente" = false AND NEW."aprovado" = false THEN --rejeitado
            IF NEW."status" = 'rejeitado' THEN
                RETURN NEW;
            END IF;

            UPDATE "ProdutoEstoque" pe
            SET "estoqueDisp" = "estoqueDisp" + pl."quantidade"
            FROM "ProdutoLote" pl
            WHERE pe."codProduto" = pl."codProduto"
                AND pe."codEstoque" = pl."codEstoque"
                AND pl."numLote" = NEW."numLote";

            UPDATE "Saida"
            SET "status" = 'rejeitado', "dataConfirmacao" = NOW()
            WHERE "codOperacao" = NEW."codOperacao";

            RETURN NEW;
        END IF;


    END;
    $$ LANGUAGE plpgsql;

-- CREATE OR REPLACE FUNCTION ajustar_estoque()
-- RETURNS TRIGGER AS $$
-- BEGIN
--     -- Rejeita as saidas pendentes
--     UPDATE "Saida" s
--     SET 
--         "aprovado" = false,
--         "pendente" = false
--     WHERE 
--         s."pendente" = true
--         AND s."codProduto" = NEW."codProduto"
--         AND s."codEstoque" = NEW."codEstoque";

--     -- Atualiza os valores em ProdutoEstoque
--     UPDATE "ProdutoEstoque" pe
--     SET 
--         pe."estoqueAtual" = NEW."valorNovo",
--         pe."estoqueDisp" = NEW."valorNovo"
--     WHERE 
--         pe."codProduto" = NEW."codProduto" 
--         AND pe."codEstoque" = NEW."codEstoque";

--     RETURN NEW;
-- END;
-- $$ LANGUAGE plpgsql;

-- FUNCOES
CREATE OR REPLACE FUNCTION atualizar_ultimo_inventario()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE "ProdutoEstoque" pe
    SET "ultimoInv" = NEW."data"
    WHERE pe."codProduto" = NEW."codProduto"
        AND pe."codEstoque" = NEW."codEstoque";
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- TRIGGERS
CREATE TRIGGER trigger_entrada
AFTER INSERT OR UPDATE ON "Entrada"
FOR EACH ROW
EXECUTE FUNCTION atualizar_estoque_entrada();

CREATE TRIGGER trigger_saida
AFTER INSERT OR UPDATE ON "Saida"
FOR EACH ROW
EXECUTE FUNCTION atualizar_estoque_saida();

-- CREATE TRIGGER trigger_ajuste
-- AFTER INSERT ON "Ajuste"
-- FOR EACH ROW
-- EXECUTE FUNCTION ajustar_estoque();

CREATE TRIGGER trigger_inventario
AFTER INSERT ON "Inventario"
FOR EACH ROW
EXECUTE FUNCTION atualizar_ultimo_inventario();

-- DROP TRIGGER IF EXISTS trigger_entrada
-- ON "Entrada";

-- DROP TRIGGER IF EXISTS trigger_requisicao
-- ON "Requisicao";

-- DROP TRIGGER IF EXISTS trigger_saida
-- ON "Saida";

-- DROP TRIGGER IF EXISTS trigger_ajuste
-- ON "Ajuste";
