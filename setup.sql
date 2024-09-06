DROP TABLE IF EXISTS "Produto" CASCADE;
DROP TABLE IF EXISTS "Categoria" CASCADE;
DROP TABLE IF EXISTS "Cotacao" CASCADE;
DROP TABLE IF EXISTS "Fornecedor" CASCADE;
DROP TABLE IF EXISTS "Restaurante" CASCADE;
DROP TABLE IF EXISTS "Estoque" CASCADE;
DROP TABLE IF EXISTS "ProdutoEstoque" CASCADE;
DROP TABLE IF EXISTS "Inventario" CASCADE;
DROP TABLE IF EXISTS "Lote" CASCADE;
DROP TABLE IF EXISTS "ProdutoLote" CASCADE;
DROP TABLE IF EXISTS "Operacao" CASCADE;
DROP TABLE IF EXISTS "Entrada" CASCADE;
DROP TABLE IF EXISTS "Ajuste" CASCADE;
DROP TABLE IF EXISTS "Saida" CASCADE;
DROP TABLE IF EXISTS "Requisicao" CASCADE;
DROP TABLE IF EXISTS "Funcionario" CASCADE;
DROP TABLE IF EXISTS "Compra" CASCADE;
DROP SEQUENCE IF EXISTS codOperacao_seq CASCADE;

CREATE TABLE "Funcionario" (
  "cpfFuncionario" char(11) PRIMARY KEY,
  "sexo" char(1),
  "telefone" bigint,
  "nome" varchar NOT NULL,
  "dataContratacao" date NOT NULL,
  "cargo" char(1) NOT NULL,
  "cnpjRestaurante" char(14)
);

CREATE TABLE "Categoria" (
  "codCategoria" serial PRIMARY KEY,
  "nome" varchar NOT NULL
);

CREATE TABLE "Produto" (
  "codProduto" serial PRIMARY KEY,
  "quantidade" real NOT NULL,
  "unidade" varchar NOT NULL,
  "nome" varchar NOT NULL,
  "descricao" varchar,
  "codCategoria" integer NOT NULL
);

CREATE TABLE "Fornecedor" (
  "cnpjFornecedor" character(14) PRIMARY KEY,
  "endereco" varchar,
  "razao" varchar UNIQUE NOT NULL,
  "nome" varchar NOT NULL,
  "telefone" bigint
);

CREATE TABLE "Restaurante" (
  "cnpjRestaurante" character(14) PRIMARY KEY,
  "endereco" varchar,
  "razao" varchar UNIQUE NOT NULL,
  "nome" varchar NOT NULL,
  "telefone" bigint,
  "cnpjMatriz" character(14),
  "cpfGerente" character(11) UNIQUE NOT NULL
);

CREATE TABLE "Cotacao" (
  "valor" money NOT NULL,
  "codProduto" integer,
  "cnpjFornecedor" character(14),
  PRIMARY KEY ("codProduto", "cnpjFornecedor")
);

CREATE TABLE "Estoque" (
  "codEstoque" serial PRIMARY KEY,
  "nome" varchar NOT NULL,
  "cnpjRestaurante" character(14) NOT NULL
);

CREATE TABLE "ProdutoEstoque" (
  "codProduto" integer,
  "codEstoque" integer,
  "estoqueMax" integer,
  "estoqueMin" integer,
  "estoqueAtual" integer,
  "estoqueDisp" integer,
  "ultimoInv" date,
  PRIMARY KEY ("codProduto", "codEstoque")
);


CREATE TABLE "Inventario" (
  "codProduto" integer,
  "codEstoque" integer,
  "data" date,
  "contagem" integer,
  "diferenca" integer,
  "ajustado" boolean,
  "cpfOperador" character(11) NOT NULL,
  PRIMARY KEY ("codProduto", "codEstoque", "data")
);

CREATE TABLE "Lote" (
  "numLote" serial PRIMARY KEY,
  "tipo" varchar
);

CREATE TABLE "ProdutoLote" (
  "codProduto" integer,
  "codEstoque" integer,
  "numLote" integer,
  "quantidade" integer NOT NULL,
  PRIMARY KEY ("codProduto", "codEstoque", "numLote")
);

CREATE TABLE "Compra" (
  "numNF" integer PRIMARY KEY,
  "codOperacao" integer,
  "cnpjFornecedor" char(14),
  "cnpjRestaurante" char(14),
  "notaFiscal" bytea NOT NULL,
  "data" date NOT NULL
);

CREATE SEQUENCE codOperacao_seq START 1;

CREATE TABLE "Entrada" (
  "codOperacao" integer PRIMARY KEY DEFAULT nextval('codOperacao_seq'),
  "descricao" varchar,
  "dataLancamento" timestamp NOT NULL DEFAULT NOW(),
  "dataConfirmacao" timestamp,
  "status" varchar(10),
  "pendente" bool NOT NULL DEFAULT true,
  "aprovado" bool NOT NULL DEFAULT false,
  "numLote" integer NOT NULL,
  "cpfEstoquista" character(11),
  "cpfOperador" character(11) NOT NULL,
  "codEstoque" integer NOT NULL
);

CREATE TABLE "Saida" (
  "codOperacao" integer PRIMARY KEY DEFAULT nextval('codOperacao_seq'),
  "descricao" varchar,
  "dataLancamento" timestamp NOT NULL DEFAULT NOW(),
  "dataConfirmacao" timestamp,
  "status" varchar(10),
  "pendente" bool NOT NULL DEFAULT true,
  "aprovado" bool NOT NULL DEFAULT false,
  "numLote" integer NOT NULL,
  "cpfEstoquista" character(11),
  "cpfOperador" character(11) NOT NULL,
  "codEstoque" integer NOT NULL
);

ALTER TABLE "Produto" ADD FOREIGN KEY ("codCategoria") REFERENCES "Categoria" ("codCategoria");

ALTER TABLE "Funcionario" ADD FOREIGN KEY ("cnpjRestaurante") REFERENCES "Restaurante" ("cnpjRestaurante");

ALTER TABLE "Restaurante" ADD FOREIGN KEY ("cnpjMatriz") REFERENCES "Restaurante" ("cnpjRestaurante");
ALTER TABLE "Restaurante" ADD FOREIGN KEY ("cpfGerente") REFERENCES "Funcionario" ("cpfFuncionario");

ALTER TABLE "Cotacao" ADD FOREIGN KEY ("codProduto") REFERENCES "Produto" ("codProduto");
ALTER TABLE "Cotacao" ADD FOREIGN KEY ("cnpjFornecedor") REFERENCES "Fornecedor" ("cnpjFornecedor");

ALTER TABLE "Estoque" ADD FOREIGN KEY ("cnpjRestaurante") REFERENCES "Restaurante" ("cnpjRestaurante");

ALTER TABLE "ProdutoEstoque" ADD FOREIGN KEY ("codProduto") REFERENCES "Produto" ("codProduto");
ALTER TABLE "ProdutoEstoque" ADD FOREIGN KEY ("codEstoque") REFERENCES "Estoque" ("codEstoque");

ALTER TABLE "Inventario" ADD FOREIGN KEY ("codProduto","codEstoque") REFERENCES "ProdutoEstoque" ("codProduto","codEstoque");
ALTER TABLE "Inventario" ADD FOREIGN KEY ("cpfOperador") REFERENCES "Funcionario" ("cpfFuncionario");
-- ALTER TABLE "Inventario" ADD FOREIGN KEY ("numLote") REFERENCES "Lote" ("numLote");

-- ALTER TABLE "Ajuste" ADD FOREIGN KEY ("codProduto","codEstoque","data") REFERENCES "Inventario" ("codProduto","codEstoque","data");

ALTER TABLE "ProdutoLote" ADD FOREIGN KEY ("codProduto","codEstoque") REFERENCES "ProdutoEstoque" ("codProduto","codEstoque");
ALTER TABLE "ProdutoLote" ADD FOREIGN KEY ("numLote") REFERENCES "Lote" ("numLote");

ALTER TABLE "Entrada" ADD FOREIGN KEY ("numLote") REFERENCES "Lote" ("numLote");
ALTER TABLE "Entrada" ADD FOREIGN KEY ("cpfEstoquista") REFERENCES "Funcionario" ("cpfFuncionario");
ALTER TABLE "Entrada" ADD FOREIGN KEY ("cpfOperador") REFERENCES "Funcionario" ("cpfFuncionario");
ALTER TABLE "Entrada" ADD CONSTRAINT lote_unico_entrada UNIQUE ("numLote");
ALTER TABLE "Entrada" ADD FOREIGN KEY ("codEstoque") REFERENCES "Estoque" ("codEstoque");

-- ALTER TABLE "Ajuste" ADD FOREIGN KEY ("numLote") REFERENCES "Lote" ("numLote");
-- ALTER TABLE "Ajuste" ADD FOREIGN KEY ("cpfEstoquista") REFERENCES "Funcionario" ("cpfFuncionario");
-- ALTER TABLE "Ajuste" ADD FOREIGN KEY ("cpfOperador") REFERENCES "Funcionario" ("cpfFuncionario");
-- ALTER TABLE "Ajuste" ADD FOREIGN KEY ("codProduto","codEstoque","data") REFERENCES "Inventario" ("codProduto","codEstoque","data");
-- ALTER TABLE "Ajuste" ADD CONSTRAINT lote_unico_ajuste UNIQUE ("numLote");

-- ALTER TABLE "Requisicao" ADD FOREIGN KEY ("numLote") REFERENCES "Lote" ("numLote");
-- ALTER TABLE "Requisicao" ADD FOREIGN KEY ("cpfEstoquista") REFERENCES "Funcionario" ("cpfFuncionario");
-- ALTER TABLE "Requisicao" ADD FOREIGN KEY ("cpfOperador") REFERENCES "Funcionario" ("cpfFuncionario");
-- ALTER TABLE "Requisicao" ADD CONSTRAINT lote_unico_requisicao UNIQUE ("numLote");
-- ALTER TABLE "Requisicao" ADD FOREIGN KEY ("codEstoque") REFERENCES "Estoque" ("codEstoque");

ALTER TABLE "Saida" ADD FOREIGN KEY ("numLote") REFERENCES "Lote" ("numLote");
ALTER TABLE "Saida" ADD FOREIGN KEY ("cpfEstoquista") REFERENCES "Funcionario" ("cpfFuncionario");
ALTER TABLE "Saida" ADD FOREIGN KEY ("cpfOperador") REFERENCES "Funcionario" ("cpfFuncionario");
-- ALTER TABLE "Saida" ADD FOREIGN KEY ("codRequisicao") REFERENCES "Requisicao" ("codOperacao");
ALTER TABLE "Saida" ADD CONSTRAINT lote_unico_saida UNIQUE ("numLote");
ALTER TABLE "Saida" ADD FOREIGN KEY ("codEstoque") REFERENCES "Estoque" ("codEstoque");
