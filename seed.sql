-- Funcionario
INSERT INTO "Funcionario" ("cpfFuncionario", "sexo", "telefone", "nome", "dataContratacao", "cargo") VALUES
('12345678901', 'M', 11987654321, 'João Silva', '2023-01-15', 'G'),
('67890123456', 'F', 11932109876, 'Lucia Mendes', '2023-03-18', 'G'),
('78901234567', 'M', 11921098765, 'Roberto Lima', '2022-08-25', 'G'),
('89012345678', 'F', 11910987654, 'Fernanda Costa', '2021-12-10', 'G'),
('90123456789', 'M', 11909876543, 'Pedro Almeida', '2023-06-05', 'G'),
('23456789012', 'F', 11976543210, 'Maria Oliveira', '2022-05-22', 'O'),
('34567890123', 'M', 11965432109, 'Carlos Souza', '2021-11-03', 'O'),
('45678901234', 'F', 11954321098, 'Ana Pereira', '2023-07-12', 'E'),
('56789012345', 'M', 11943210987, 'José Fernandes', '2022-09-30', 'E');

-- Categoria
INSERT INTO "Categoria" ("nome") VALUES
('Bebidas'),
('Laticínios'),
('Carnes'),
('Hortifrúti'),
('Grãos');

-- Produto
INSERT INTO "Produto" ("unidade", "quantidade", "nome", "descricao", "codCategoria") VALUES
('kg', 5.0, 'Arroz', 'Arroz branco tipo 1', 5),
('lt', 2.0, 'Leite', 'Leite integral', 2),
('un', 12.0, 'Cerveja', 'Cerveja Pilsen 350ml', 1),
('kg', 1.5, 'Tomate', 'Tomate italiano', 4),
('kg', 3.0, 'Carne bovina', 'Contrafilé', 3);

-- Fornecedor
INSERT INTO "Fornecedor" ("cnpjFornecedor", "endereco", "razao", "nome", "telefone") VALUES
('12345678000199', 'Rua A, 123', 'Fornecedor A Ltda', 'Fornecedor A', 1234567890),
('23456789000188', 'Rua B, 456', 'Fornecedor B Ltda', 'Fornecedor B', 2345678901),
('34567890000177', 'Rua C, 789', 'Fornecedor C Ltda', 'Fornecedor C', 3456789012),
('45678901000166', 'Rua D, 101', 'Fornecedor D Ltda', 'Fornecedor D', 4567890123),
('56789012000155', 'Rua E, 202', 'Fornecedor E Ltda', 'Fornecedor E', 5678901234);

-- Restaurante
INSERT INTO "Restaurante" ("cnpjRestaurante", "endereco", "razao", "nome", "telefone", "cnpjMatriz", "cpfGerente") VALUES
('98765432000199', 'Avenida X, 987', 'Restaurante X Ltda', 'Restaurante X', 9876543210, NULL, '12345678901'),
('87654321000188', 'Avenida Y, 876', 'Restaurante Y Ltda', 'Restaurante Y', 8765432109, '98765432000199', '67890123456'),
('76543210000177', 'Avenida Z, 765', 'Restaurante Z Ltda', 'Restaurante Z', 7654321098, '98765432000199', '78901234567'),
('65432100000166', 'Rua W, 654', 'Restaurante W Ltda', 'Restaurante W', 6543210987, '87654321000188', '89012345678'),
('54321000000155', 'Rua V, 543', 'Restaurante V Ltda', 'Restaurante V', 5432109876, NULL, '90123456789');

-- Cotacao
INSERT INTO "Cotacao" ("valor", "codProduto", "cnpjFornecedor") VALUES
('15.00', 1, '12345678000199'),
('4.50', 2, '23456789000188'),
('2.00', 3, '34567890000177'),
('3.20', 4, '45678901000166'),
('30.00', 5, '56789012000155');

-- Estoque
INSERT INTO "Estoque" ("nome", "cnpjRestaurante") VALUES
('Estoque Central', '98765432000199'),
('Estoque Secundário', '98765432000199'),
('Estoque de Bebidas', '98765432000199'),
('Estoque de Hortifrúti', '98765432000199'),
('Estoque de Carnes', '98765432000199');

-- ProdutoEstoque
INSERT INTO "ProdutoEstoque" ("codProduto", "codEstoque", "estoqueMax", "estoqueMin", "estoqueAtual", "estoqueDisp", "ultimoInv") VALUES
(1, 1, 100, 20, 0, 0, '2024-08-01'),
(2, 1, 200, 50, 0, 0, '2024-08-02'),
(3, 1, 300, 100, 0, 0, '2024-08-03'),
(4, 1, 150, 30, 0, 0, '2024-08-04'),
(5, 1, 400, 150, 0, 0, '2024-08-05');

-- Inventario
INSERT INTO "Inventario" ("codProduto", "codEstoque", "dataInv", "contagem", "cpfEstoquista") VALUES
(1, 1, '2024-08-01', 45, '56789012345'),
(2, 1, '2024-08-02', 115, '45678901234'),
(3, 1, '2024-08-03', 240, '56789012345'),
(4, 1, '2024-08-04', 75, '45678901234'),
(5, 1, '2024-08-05', 330, '56789012345');

-- Lote
INSERT INTO "Lote" ("tipo") VALUES
('entrada'),
('entrada'),
('entrada'),
('entrada'),
('entrada'),
('requisicao'),
('requisicao'),
('requisicao'),
('requisicao'),
('requisicao'),
('saida'),
('saida'),
('saida'),
('saida'),
('saida'),
('ajuste'),
('ajuste'),
('ajuste'),
('ajuste'),
('ajuste');

-- ProdutoLote
INSERT INTO "ProdutoLote" ("codProduto", "codEstoque", "numLote", "quantidade") VALUES
(1, 1, 1, 10),
(2, 1, 1, 20),
(3, 1, 1, 30),
(4, 1, 1, 40),
(5, 1, 1, 50),

(1, 1, 6, 10),
(2, 1, 6, 10),
(3, 1, 6, 10),
(4, 1, 6, 10),
(5, 1, 6, 10),

(1, 1, 11, 10),
(2, 1, 11, 10),
(3, 1, 11, 10),
(4, 1, 11, 10),
(5, 1, 11, 10),

(1, 1, 16, 10),
(2, 1, 16, 10),
(3, 1, 16, 10),
(4, 1, 16, 10),
(5, 1, 16, 10);


-- Entrada
INSERT INTO "Entrada" ("descricao", "dataLancamento", "dataConfirmacao", "status", "pendente", "aprovado", "numLote", "cpfEstoquista", "cpfOperador") VALUES
('Entrada de carnes', '2024-08-20', '2024-08-21', 'aprovado', false, true, 1, '12345678901', '23456789012'),
('Entrada de bebidas', '2024-08-22', '2024-08-23', 'pendente', true, false, 2, '23456789012', '34567890123'),
('Entrada de produtos de limpeza', '2024-08-24', '2024-08-25', 'aprovado', false, true, 3, '34567890123', '45678901234'),
('Entrada de itens de higiene', '2024-08-26', '2024-08-27', 'aprovado', false, true, 4, '45678901234', '56789012345'),
('Entrada de ingredientes perecíveis', '2024-08-28', '2024-08-29', 'pendente', true, false, 5, '56789012345', '12345678901');

-- Compra 
-- INSERT INTO "Compra" ("codOperacao", "cnpjFornecedor", "cnpjRestaurante", "notaFiscal", "data", "quantidade") VALUES
-- (1, '12345678000199', '98765432000199', decode('DEADBEEF', 'hex'), '2024-08-20', 100),
-- (2, '23456789000188', '98765432000199', decode('CAFEBABE', 'hex'), '2024-08-22', 200),
-- (3, '34567890000177', '98765432000199', decode('BEEFFACE', 'hex'), '2024-08-24', 150),
-- (4, '45678901000166', '98765432000199', decode('FEEDFACE', 'hex'), '2024-08-26', 300),
-- (5, '56789012000155', '98765432000199', decode('BADF00D', 'hex'), '2024-08-28', 250);

-- Requisicao
INSERT INTO "Requisicao" ("descricao", "dataLancamento", "dataConfirmacao", "status", "pendente", "aprovado", "numLote", "cpfEstoquista", "cpfOperador") VALUES
('Requisição de carnes', '2024-08-25', '2024-08-26', 'aprovado', true, false, 6, '56789012345', '12345678901'),
('Requisição de bebidas', '2024-08-26', NULL, 'pendente', true, false, 7, '45678901234', '23456789012'),
('Requisição de produtos de limpeza', '2024-08-27', '2024-08-28', 'aprovado', true, false, 8, '34567890123', '34567890123'),
('Requisição de itens de higiene', '2024-08-28', NULL, 'pendente', true, false, 9, '23456789012', '45678901234'),
('Requisição de ingredientes', '2024-08-29', '2024-08-30', 'aprovado', true, false, 10, '12345678901', '56789012345');

-- Saida
-- INSERT INTO "Saida" ("descricao", "dataLancamento", "dataConfirmacao", "status", "pendente", "aprovado", "numLote", "cpfEstoquista", "cpfOperador", "codRequisicao") VALUES
-- ('Saída de ingredientes para preparo', '2024-08-20', '2024-08-21', 'aprovado', false, true, 11, '12345678901', '23456789012', 6),
-- ('Saída de bebidas para reposição', '2024-08-22', '2024-08-23', 'aprovado', false, true, 12, '23456789012', '34567890123', 7),
-- ('Saída de produtos de limpeza', '2024-08-24', '2024-08-25', 'aprovado', false, true, 13, '34567890123', '45678901234', 8),
-- ('Saída de itens de higiene', '2024-08-26', '2024-08-27', 'aprovado', false, true, 14, '45678901234', '56789012345', 9),
-- ('Saída de carnes para preparo', '2024-08-28', '2024-08-29', 'aprovado', false, true, 15, '56789012345', '12345678901', 10);

-- Ajuste
INSERT INTO "Ajuste" ("descricao", "dataLancamento", "dataConfirmacao", "status", "pendente", "aprovado", "numLote", "cpfEstoquista", "cpfOperador", "codProduto", "codEstoque", "dataInv") VALUES
('Correção de contagem', '2024-08-10', '2024-08-12', 'confirmado', false, true, 16, '56789012345', '23456789012', 1, 1, '2024-08-01'),
('Ajuste de estoque inicial', '2024-08-11', NULL, 'pendente', true, false, 17, '45678901234', '34567890123', 2, 1, '2024-08-02'),
('Ajuste pós-inventário', '2024-08-15', '2024-08-16', 'confirmado', false, true, 18, '56789012345', '23456789012', 3, 1, '2024-08-03'),
('Correção de lote', '2024-08-20', NULL, 'pendente', true, false, 19, '45678901234', '34567890123', 4, 1, '2024-08-04'),
('Ajuste final de estoque', '2024-08-25', '2024-08-26', 'confirmado', false, true, 20, '56789012345', '23456789012', 5, 1, '2024-08-05');
