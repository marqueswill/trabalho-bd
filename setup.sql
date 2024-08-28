DROP TABLE IF EXISTS "TBL_Produto" CASCADE;
DROP TABLE IF EXISTS "TBL_Categoria" CASCADE;
DROP TABLE IF EXISTS "TBL_Cotacao" CASCADE;
DROP TABLE IF EXISTS "TBL_Fornecedor" CASCADE;
DROP TABLE IF EXISTS "TBL_Restaurante" CASCADE;
DROP TABLE IF EXISTS "TBL_Estoque" CASCADE;
DROP TABLE IF EXISTS "TBL_ProdutoEstoque" CASCADE;
DROP TABLE IF EXISTS "TBL_Inventario" CASCADE;
DROP TABLE IF EXISTS "TBL_Lote" CASCADE;
DROP TABLE IF EXISTS "TBL_ProdutoLote" CASCADE;
DROP TABLE IF EXISTS "TBL_Operacao" CASCADE;
DROP TABLE IF EXISTS "TBL_Entrada" CASCADE;
DROP TABLE IF EXISTS "TBL_Ajuste" CASCADE;
DROP TABLE IF EXISTS "TBL_Saida" CASCADE;
DROP TABLE IF EXISTS "TBL_Requisicao" CASCADE;
DROP TABLE IF EXISTS "TBL_Funcionario" CASCADE;
DROP TABLE IF EXISTS "TBL_Compra" CASCADE;
DROP SEQUENCE IF EXISTS codOperacao_seq CASCADE;

CREATE TABLE "TBL_Categoria" (
  "codCategoria" serial PRIMARY KEY,
  "nome" varchar NOT NULL
);

-- CREATE TABLE "TBL_Produto" (
--   "codProduto" serial PRIMARY KEY,
--   "uncodade" varchar NOT NULL,
--   "quantcodade" real NOT NULL,
--   "nome" varchar NOT NULL,
--   "descricao" varchar,
--   "codCategoria" integer NOT NULL
-- );

-- CREATE TABLE "TBL_Fornecedor" (
--   "cnpjFornecedor" character(14) PRIMARY KEY,
--   "endereco" varchar,
--   "razao" varchar UNIQUE NOT NULL,
--   "nome" varchar NOT NULL,
--   "telefone" bigint
-- );

-- CREATE TABLE "TBL_Restaurante" (
--   "cnpjRestaurante" character(14) PRIMARY KEY,
--   "endereco" varchar,
--   "razao" varchar UNIQUE NOT NULL,
--   "nome" varchar NOT NULL,
--   "telefone" bigint,
--   "cnpjMatriz" character(14),
--   "cpfGerente" character(11) UNIQUE NOT NULL
-- );

-- CREATE TABLE "TBL_Cotacao" (
--   "valor" money NOT NULL,
--   "codProduto" integer,
--   "cnpjFornecedor" character(14),
--   PRIMARY KEY ("codProduto", "cnpjFornecedor")
-- );

-- CREATE TABLE "TBL_Estoque" (
--   "codEstoque" serial PRIMARY KEY,
--   "nome" varchar NOT NULL,
--   "cnpjRestaurante" character(14) NOT NULL
-- );

-- CREATE TABLE "TBL_ProdutoEstoque" (
--   "codProduto" integer,
--   "codEstoque" integer,
--   "estoqueMax" integer,
--   "estoqueMin" integer,
--   "estoqueAtual" integer,
--   "estoqueDisp" integer,
--   "ultimoInv" date,
--   PRIMARY KEY ("codProduto", "codEstoque")
-- );

-- CREATE TABLE "TBL_Funcionario" (
--   "cpfFuncionario" char(11) PRIMARY KEY,
--   "sexo" char(1),
--   "telefone" bigint,
--   "nome" varchar NOT NULL,
--   "dataContratacao" date NOT NULL,
--   "cargo" char(1) NOT NULL
-- );

-- CREATE TABLE "TBL_Inventario" (
--   "codProduto" integer,
--   "codEstoque" integer,
--   "dataInv" date,
--   "contagem" integer,
--   "cpfEstoquista" character(11) NOT NULL,
--   PRIMARY KEY ("codProduto", "codEstoque", "dataInv")
-- );

-- CREATE TABLE "TBL_Lote" (
--   "numLote" integer PRIMARY KEY,
--   "cpnjFornecedor" char(11)
-- );

-- CREATE TABLE "TBL_ProdutoLote" (
--   "codProduto" integer,
--   "codEstoque" integer,
--   "numLote" integer,
--   PRIMARY KEY ("codProduto", "codEstoque", "numLote")
-- );

-- CREATE TABLE "TBL_Compra" (
--   "codOperacao" integer,
--   "cnpjFornecedor" char(14),
--   "cnpjRestaurante" char(14),
--   "notaFiscal" bytea NOT NULL,
--   "data" date NOT NULL,
--   PRIMARY KEY ("codOperacao", "cnpjFornecedor", "cnpjRestaurante")
-- );

-- CREATE SEQUENCE codOperacao_seq START 1;

-- CREATE TABLE "TBL_Entrada" (
--   "codOperacao" integer PRIMARY KEY DEFAULT nextval('codOperacao_seq'),
--   "descricao" varchar,
--   "dataLancamento" date NOT NULL,
--   "dataConfirmacao" date,
--   "status" varchar(10) DEFAULT 'pendente',
--   "pendente" bool NOT NULL DEFAULT true,
--   "aprovado" bool NOT NULL DEFAULT false,
--   "numLote" integer NOT NULL,
--   "cpfEstoquista" character(11),
--   "cpfOperador" character(11) NOT NULL,
--   "notaFiscal" bytea
-- );

-- CREATE TABLE "TBL_Ajuste" (
--   "codOperacao" integer PRIMARY KEY DEFAULT nextval('codOperacao_seq'),
--   "descricao" varchar,
--   "dataLancamento" date NOT NULL,
--   "dataConfirmacao" date,
--   "status" varchar(10) DEFAULT 'pendente',
--   "pendente" bool NOT NULL DEFAULT true,
--   "aprovado" bool NOT NULL DEFAULT false,
--   "numLote" integer NOT NULL,
--   "cpfEstoquista" character(11),
--   "cpfOperador" character(11) NOT NULL,
--   "codProduto" integer NOT NULL,
--   "codEstoque" integer NOT NULL,
--   "dataInv" date NOT NULL
-- );

-- CREATE TABLE "TBL_Requisicao" (
--   "codOperacao" integer PRIMARY KEY DEFAULT nextval('codOperacao_seq'),
--   "descricao" varchar,
--   "dataLancamento" date NOT NULL,
--   "dataConfirmacao" date,
--   "status" varchar(10) DEFAULT 'pendente',
--   "pendente" bool NOT NULL DEFAULT true,
--   "aprovado" bool NOT NULL DEFAULT false,
--   "numLote" integer NOT NULL,
--   "cpfEstoquista" character(11),
--   "cpfOperador" character(11) NOT NULL
-- );

-- CREATE TABLE "TBL_Saida" (
--   "codOperacao" integer PRIMARY KEY DEFAULT nextval('codOperacao_seq'),
--   "descricao" varchar,
--   "dataLancamento" date NOT NULL,
--   "dataConfirmacao" date,
--   "status" varchar(10) DEFAULT 'pendente',
--   "pendente" bool NOT NULL DEFAULT true,
--   "aprovado" bool NOT NULL DEFAULT false,
--   "numLote" integer NOT NULL,
--   "cpfEstoquista" character(11),
--   "cpfOperador" character(11) NOT NULL
-- );

-- ALTER TABLE "TBL_Produto" ADD FOREIGN KEY ("codCategoria") REFERENCES "TBL_Categoria" ("codCategoria");

-- ALTER TABLE "TBL_Restaurante" ADD FOREIGN KEY ("cnpjMatriz") REFERENCES "TBL_Restaurante" ("cnpjRestaurante");

-- ALTER TABLE "TBL_Restaurante" ADD FOREIGN KEY ("cpfGerente") REFERENCES "TBL_Funcionario" ("cpfFuncionario");

-- ALTER TABLE "TBL_Cotacao" ADD FOREIGN KEY ("codProduto") REFERENCES "TBL_Produto" ("codProduto");

-- ALTER TABLE "TBL_Cotacao" ADD FOREIGN KEY ("cnpjFornecedor") REFERENCES "TBL_Fornecedor" ("cnpjFornecedor");

-- ALTER TABLE "TBL_Estoque" ADD FOREIGN KEY ("cnpjRestaurante") REFERENCES "TBL_Restaurante" ("cnpjRestaurante");

-- ALTER TABLE "TBL_ProdutoEstoque" ADD FOREIGN KEY ("codProduto") REFERENCES "TBL_Produto" ("codProduto");

-- ALTER TABLE "TBL_ProdutoEstoque" ADD FOREIGN KEY ("codEstoque") REFERENCES "TBL_Estoque" ("codEstoque");

-- ALTER TABLE "TBL_Inventario" ADD FOREIGN KEY ("codProduto","codEstoque") REFERENCES "TBL_ProdutoEstoque" ("codProduto","codEstoque");

-- ALTER TABLE "TBL_Inventario" ADD FOREIGN KEY ("cpfEstoquista") REFERENCES "TBL_Funcionario" ("cpfFuncionario");

-- ALTER TABLE "TBL_ProdutoLote" ADD FOREIGN KEY ("codProduto","codEstoque") REFERENCES "TBL_ProdutoEstoque" ("codProduto","codEstoque");

-- ALTER TABLE "TBL_ProdutoLote" ADD FOREIGN KEY ("numLote") REFERENCES "TBL_Lote" ("numLote");

-- ALTER TABLE "TBL_Compra" ADD FOREIGN KEY ("cnpjFornecedor") REFERENCES "TBL_Fornecedor" ("cnpjFornecedor");

-- ALTER TABLE "TBL_Compra" ADD FOREIGN KEY ("cnpjRestaurante") REFERENCES "TBL_Restaurante" ("cnpjRestaurante");

-- ALTER TABLE "TBL_Compra" ADD FOREIGN KEY ("codOperacao") REFERENCES "TBL_Entrada" ("codOperacao");

-- ALTER TABLE "TBL_Entrada" ADD FOREIGN KEY ("numLote") REFERENCES "TBL_Lote" ("numLote");

-- ALTER TABLE "TBL_Entrada" ADD FOREIGN KEY ("cpfEstoquista") REFERENCES "TBL_Funcionario" ("cpfFuncionario");

-- ALTER TABLE "TBL_Entrada" ADD FOREIGN KEY ("cpfOperador") REFERENCES "TBL_Funcionario" ("cpfFuncionario");

-- ALTER TABLE "TBL_Ajuste" ADD FOREIGN KEY ("numLote") REFERENCES "TBL_Lote" ("numLote");

-- ALTER TABLE "TBL_Ajuste" ADD FOREIGN KEY ("cpfEstoquista") REFERENCES "TBL_Funcionario" ("cpfFuncionario");

-- ALTER TABLE "TBL_Ajuste" ADD FOREIGN KEY ("cpfOperador") REFERENCES "TBL_Funcionario" ("cpfFuncionario");

-- ALTER TABLE "TBL_Ajuste" ADD FOREIGN KEY ("codProduto","codEstoque","dataInv") REFERENCES "TBL_Inventario" ("codProduto","codEstoque","dataInv");

-- ALTER TABLE "TBL_Requisicao" ADD FOREIGN KEY ("numLote") REFERENCES "TBL_Lote" ("numLote");

-- ALTER TABLE "TBL_Requisicao" ADD FOREIGN KEY ("cpfEstoquista") REFERENCES "TBL_Funcionario" ("cpfFuncionario");

-- ALTER TABLE "TBL_Requisicao" ADD FOREIGN KEY ("cpfOperador") REFERENCES "TBL_Funcionario" ("cpfFuncionario");

-- ALTER TABLE "TBL_Saida" ADD FOREIGN KEY ("codOperacao") REFERENCES "TBL_Requisicao" ("codOperacao");

-- ALTER TABLE "TBL_Saida" ADD FOREIGN KEY ("numLote") REFERENCES "TBL_Lote" ("numLote");

-- ALTER TABLE "TBL_Saida" ADD FOREIGN KEY ("cpfEstoquista") REFERENCES "TBL_Funcionario" ("cpfFuncionario");

-- ALTER TABLE "TBL_Saida" ADD FOREIGN KEY ("cpfOperador") REFERENCES "TBL_Funcionario" ("cpfFuncionario");
