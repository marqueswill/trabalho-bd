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
  "cargo" char(1) NOT NULL
);

CREATE TABLE "Categoria" (
  "codCategoria" serial PRIMARY KEY,
  "nome" varchar NOT NULL
);

CREATE TABLE "Produto" (
  "codProduto" serial PRIMARY KEY,
  "unidade" varchar NOT NULL,
  "quantidade" real NOT NULL,
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
  "dataInv" date,
  "contagem" integer,
  "cpfEstoquista" character(11) NOT NULL,
  PRIMARY KEY ("codProduto", "codEstoque", "dataInv")
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
  "codOperacao" integer,
  "cnpjFornecedor" char(14),
  "cnpjRestaurante" char(14),
  "notaFiscal" bytea NOT NULL,
  "data" date NOT NULL,
  "quantidade" integer NOT NULL,
  PRIMARY KEY ("codOperacao", "cnpjFornecedor", "cnpjRestaurante")
);

CREATE SEQUENCE codOperacao_seq START 1;

CREATE TABLE "Entrada" (
  "codOperacao" integer PRIMARY KEY DEFAULT nextval('codOperacao_seq'),
  "descricao" varchar,
  "dataLancamento" date NOT NULL,
  "dataConfirmacao" date,
  "status" varchar(10) DEFAULT 'pendente',
  "pendente" bool NOT NULL DEFAULT true,
  "aprovado" bool NOT NULL DEFAULT false,
  "numLote" integer NOT NULL,
  "cpfEstoquista" character(11),
  "cpfOperador" character(11) NOT NULL
);

CREATE TABLE "Requisicao" (
  "codOperacao" integer PRIMARY KEY DEFAULT nextval('codOperacao_seq'),
  "descricao" varchar,
  "dataLancamento" date NOT NULL,
  "dataConfirmacao" date,
  "status" varchar(10) DEFAULT 'pendente',
  "pendente" bool NOT NULL DEFAULT true,
  "aprovado" bool NOT NULL DEFAULT false,
  "numLote" integer NOT NULL,
  "cpfEstoquista" character(11),
  "cpfOperador" character(11) NOT NULL
);

CREATE TABLE "Saida" (
  "codOperacao" integer PRIMARY KEY DEFAULT nextval('codOperacao_seq'),
  "descricao" varchar,
  "dataLancamento" date NOT NULL,
  "dataConfirmacao" date,
  "status" varchar(10) DEFAULT 'pendente',
  "pendente" bool NOT NULL DEFAULT false,
  "aprovado" bool NOT NULL DEFAULT true,
  "numLote" integer NOT NULL,
  "cpfEstoquista" character(11),
  "cpfOperador" character(11) NOT NULL,
  "codRequisicao" integer NOT NULL
);

CREATE TABLE "Ajuste" (
  "codOperacao" integer PRIMARY KEY DEFAULT nextval('codOperacao_seq'),
  "descricao" varchar,
  "dataLancamento" date NOT NULL,
  "dataConfirmacao" date,
  "status" varchar(10) DEFAULT 'pendente',
  "pendente" bool NOT NULL DEFAULT true,
  "aprovado" bool NOT NULL DEFAULT false,
  "numLote" integer NOT NULL,
  "cpfEstoquista" character(11),
  "cpfOperador" character(11) NOT NULL,
  "codProduto" integer NOT NULL,
  "codEstoque" integer NOT NULL,
  "dataInv" date NOT NULL
);

ALTER TABLE "Produto" ADD FOREIGN KEY ("codCategoria") REFERENCES "Categoria" ("codCategoria");

ALTER TABLE "Restaurante" ADD FOREIGN KEY ("cnpjMatriz") REFERENCES "Restaurante" ("cnpjRestaurante");
ALTER TABLE "Restaurante" ADD FOREIGN KEY ("cpfGerente") REFERENCES "Funcionario" ("cpfFuncionario");

ALTER TABLE "Cotacao" ADD FOREIGN KEY ("codProduto") REFERENCES "Produto" ("codProduto");
ALTER TABLE "Cotacao" ADD FOREIGN KEY ("cnpjFornecedor") REFERENCES "Fornecedor" ("cnpjFornecedor");

ALTER TABLE "Estoque" ADD FOREIGN KEY ("cnpjRestaurante") REFERENCES "Restaurante" ("cnpjRestaurante");

ALTER TABLE "ProdutoEstoque" ADD FOREIGN KEY ("codProduto") REFERENCES "Produto" ("codProduto");
ALTER TABLE "ProdutoEstoque" ADD FOREIGN KEY ("codEstoque") REFERENCES "Estoque" ("codEstoque");

ALTER TABLE "Inventario" ADD FOREIGN KEY ("codProduto","codEstoque") REFERENCES "ProdutoEstoque" ("codProduto","codEstoque");
ALTER TABLE "Inventario" ADD FOREIGN KEY ("cpfEstoquista") REFERENCES "Funcionario" ("cpfFuncionario");

ALTER TABLE "ProdutoLote" ADD FOREIGN KEY ("codProduto","codEstoque") REFERENCES "ProdutoEstoque" ("codProduto","codEstoque");
ALTER TABLE "ProdutoLote" ADD FOREIGN KEY ("numLote") REFERENCES "Lote" ("numLote");

ALTER TABLE "Ajuste" ADD FOREIGN KEY ("cpfOperador") REFERENCES "Funcionario" ("cpfFuncionario");
ALTER TABLE "Ajuste" ADD FOREIGN KEY ("codProduto","codEstoque","dataInv") REFERENCES "Inventario" ("codProduto","codEstoque","dataInv");

ALTER TABLE "Requisicao" ADD FOREIGN KEY ("numLote") REFERENCES "Lote" ("numLote");
ALTER TABLE "Requisicao" ADD FOREIGN KEY ("cpfEstoquista") REFERENCES "Funcionario" ("cpfFuncionario");
ALTER TABLE "Requisicao" ADD FOREIGN KEY ("cpfOperador") REFERENCES "Funcionario" ("cpfFuncionario");

ALTER TABLE "Saida" ADD FOREIGN KEY ("numLote") REFERENCES "Lote" ("numLote");
ALTER TABLE "Saida" ADD FOREIGN KEY ("cpfEstoquista") REFERENCES "Funcionario" ("cpfFuncionario");
ALTER TABLE "Saida" ADD FOREIGN KEY ("cpfOperador") REFERENCES "Funcionario" ("cpfFuncionario");
ALTER TABLE "Saida" ADD FOREIGN KEY ("codRequisicao") REFERENCES "Requisicao" ("codOperacao");