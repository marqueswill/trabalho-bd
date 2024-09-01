-- FUNCOES
CREATE OR REPLACE FUNCTION atualizar_estoque_entrada()
RETURNS TRIGGER AS $$
BEGIN
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
    UPDATE "ProdutoEstoque" pe
    SET "estoqueDisp" = "estoqueDisp" - pl."quantidade"
    FROM "ProdutoLote" pl
    WHERE pe."codProduto" = pl."codProduto"
        AND pe."codEstoque" = pl."codEstoque"
        AND pl."numLote" = NEW."numLote";
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION rejeitar_requisicao()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE "ProdutoEstoque" pe
    SET "estoqueDisp" = "estoqueDisp" + pl."quantidade"
    FROM "ProdutoLote" pl
    WHERE pe."codProduto" = pl."codProduto"
        AND pe."codEstoque" = pl."codEstoque"
        AND pl."numLote" = NEW."numLote";
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION aprovar_requisicao()
RETURNS TRIGGER AS $$
BEGIN
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
        "codRequisicao"
    ) 
    VALUES (
        NEW."descricao", 
        NEW."dataLancamento", 
        NEW."dataConfirmacao", 
        NEW."status", 
        NEW."pendente",
        NEW."aprovado", 
        NEW."numLote", 
        NEW."cpfEstoquista", 
        NEW."cpfOperador", 
        NEW."codOperacao"
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION ajustar_estoque()
RETURNS TRIGGER AS $$
BEGIN
    -- Atualiza os valores em ProdutoEstoque
    UPDATE "ProdutoEstoque" pe
    SET 
        pe."estoqueAtual" = NEW."valorNovo",
        pe."estoqueDisp" = NEW."valorNovo"
    WHERE 
        pe."codProduto" = NEW."codProduto" 
        AND pe."codEstoque" = NEW."codEstoque";

    -- Atualiza os valores em Requisicao
    UPDATE "Requisicao" req
    SET 
        "aprovado" = false,
        "pendente" = false
    WHERE 
        req."pendente" = true
        AND req."codProduto" = NEW."codProduto"
        AND req."codEstoque" = NEW."codEstoque";

    RETURN NEW;
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

CREATE TRIGGER trigger_requisicao_pendente
AFTER INSERT OR UPDATE ON "Requisicao"
FOR EACH ROW
WHEN (NEW."aprovado" = false AND NEW."pendente" = true)
EXECUTE FUNCTION atualizar_estoque_requisicao();

CREATE TRIGGER trigger_requisicao_rejeitada
AFTER INSERT OR UPDATE ON "Requisicao"
FOR EACH ROW
WHEN (NEW."aprovado" = false AND NEW."pendente" = false)
EXECUTE FUNCTION rejeitar_requisicao();

CREATE TRIGGER trigger_requisicao_aprovada
AFTER INSERT OR UPDATE ON "Requisicao"
FOR EACH ROW
WHEN (NEW."aprovado" = true AND NEW."pendente" = false)
EXECUTE FUNCTION aprovar_requisicao();

CREATE TRIGGER trigger_ajuste
AFTER INSERT OR UPDATE ON "Ajuste"
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
