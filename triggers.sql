-- FUNCOES
CREATE OR REPLACE FUNCTION atualizar_estoque_entrada()
RETURNS TRIGGER AS $$
BEGIN
    -- IF NEW."pendente" = true AND NEW."aprovado" = false THEN --pendente
    --     RETURN NEW;
    -- END IF;

    -- IF NEW."pendente" = false AND NEW."aprovado" = true THEN --aprovado
    --     RETURN NEW;
    -- END IF;

    -- IF NEW."pendente" = false AND NEW."aprovado" = false THEN --rejeitado
    --     RETURN NEW;
    -- END IF;

    NEW."status" := 'aprovado';
    UPDATE "ProdutoEstoque" pe
    SET "estoqueAtual" = "estoqueAtual" + pl."quantidade",
        "estoqueDisp" = "estoqueDisp" + pl."quantidade"
    FROM "ProdutoLote" pl
    WHERE pe."codProduto" = pl."codProduto"
        AND pe."codEstoque" = pl."codEstoque"
        AND pl."numLote" = NEW."numLote";
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION atualizar_estoque_saida()
RETURNS TRIGGER AS $$
BEGIN
    -- IF NEW."pendente" = true AND NEW."aprovado" = false THEN --pendente
    --     RETURN NEW;
    -- END IF;

    -- IF NEW."pendente" = false AND NEW."aprovado" = true THEN --aprovado
    --     RETURN NEW;
    -- END IF;

    -- IF NEW."pendente" = false AND NEW."aprovado" = false THEN --rejeitado
    --     RETURN NEW;
    -- END IF;

    NEW."status" := 'aprovado';
    UPDATE "ProdutoEstoque" pe
    SET "estoqueAtual" = "estoqueAtual" - pl."quantidade"
    FROM "ProdutoLote" pl
    WHERE pe."codProduto" = pl."codProduto"
        AND pe."codEstoque" = pl."codEstoque"
        AND pl."numLote" = NEW."numLote";
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION atualizar_estoque_requisicao()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW."pendente" = true AND NEW."aprovado" = false THEN --pendente

        UPDATE "ProdutoEstoque" pe
        SET "estoqueDisp" = "estoqueDisp" - pl."quantidade"
        FROM "ProdutoLote" pl
        WHERE pe."codProduto" = pl."codProduto"
            AND pe."codEstoque" = pl."codEstoque"
            AND pl."numLote" = NEW."numLote";
        RETURN NEW;

        
    END IF;

    IF NEW."pendente" = false AND NEW."aprovado" = true THEN --aprovado
        IF NEW."status" = 'aprovado' THEN
            RETURN NEW;
        END IF;

        INSERT INTO "Saida" (
            "descricao", 
            "dataLancamento", 
            "dataConfirmacao", 
            "status", 
            "pendente",
            "aprovado", 
            "numLote", 
            "cpfEstoquista", 
            "cpfOperador",
            "codRequisicao",
            "codEstoque"
        ) 
        VALUES (
            NEW."descricao", 
            NEW."dataLancamento", 
            NEW."dataConfirmacao", 
            'aprovado', 
            false,
            true, 
            NEW."numLote", 
            NEW."cpfEstoquista", 
            NEW."cpfOperador", 
            NEW."codOperacao",
            NEW."codEstoque"
        );

        UPDATE "Requisicao"
        SET "status" = 'aprovado'
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

        UPDATE "Requisicao"
        SET "status" = 'rejeitado'
        WHERE "codOperacao" = NEW."codOperacao";

        RETURN NEW;
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION ajustar_estoque()
RETURNS TRIGGER AS $$
BEGIN
    -- Rejeita as requisições pendentes
    UPDATE "Requisicao" req
    SET 
        "aprovado" = false,
        "pendente" = false
    WHERE 
        req."pendente" = true
        AND req."codProduto" = NEW."codProduto"
        AND req."codEstoque" = NEW."codEstoque";

    RETURN NEW;

    -- Atualiza os valores em ProdutoEstoque
    UPDATE "ProdutoEstoque" pe
    SET 
        pe."estoqueAtual" = NEW."valorNovo",
        pe."estoqueDisp" = NEW."valorNovo"
    WHERE 
        pe."codProduto" = NEW."codProduto" 
        AND pe."codEstoque" = NEW."codEstoque";

END;
$$ LANGUAGE plpgsql;


-- TRIGGERS
CREATE TRIGGER trigger_entrada
AFTER INSERT OR UPDATE ON "Entrada"
FOR EACH ROW
WHEN (NEW."aprovado" = true AND NEW."pendente" = false)
EXECUTE FUNCTION atualizar_estoque_entrada();

CREATE TRIGGER trigger_saida
AFTER INSERT OR UPDATE ON "Saida"
FOR EACH ROW
WHEN (NEW."aprovado" = true AND NEW."pendente" = false)
EXECUTE FUNCTION atualizar_estoque_saida();

CREATE TRIGGER trigger_requisicao
AFTER INSERT OR UPDATE ON "Requisicao"
FOR EACH ROW
EXECUTE FUNCTION atualizar_estoque_requisicao();

CREATE TRIGGER trigger_ajuste
AFTER INSERT ON "Ajuste"
FOR EACH ROW
EXECUTE FUNCTION ajustar_estoque();

-- DROP TRIGGER IF EXISTS trigger_entrada
-- ON "Entrada";

-- DROP TRIGGER IF EXISTS trigger_requisicao
-- ON "Requisicao";

-- DROP TRIGGER IF EXISTS trigger_saida
-- ON "Saida";

-- DROP TRIGGER IF EXISTS trigger_ajuste
-- ON "Ajuste";
