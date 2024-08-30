-- Funcionario
INSERT INTO "Funcionario" ("cpfFuncionario", "sexo", "telefone", "nome", "dataContratacao", "cargo") VALUES
('12345678901', 'M', 11987654321, 'João Silva', '2023-01-15', 'G'),
('23456789012', 'F', 11976543210, 'Maria Oliveira', '2022-05-22', 'O'),
('34567890123', 'M', 11965432109, 'Carlos Souza', '2021-11-03', 'O'),
('45678901234', 'F', 11954321098, 'Ana Pereira', '2023-07-12', 'E'),
('56789012345', 'M', 11943210987, 'José Fernandes', '2022-09-30', 'E');

-- Categoria

-- Produto

-- Fornecedor

-- Cotacao

-- Restaurante

-- Estoque

-- ProdutoEstoque

-- Inventario

-- Lote
INSERT INTO "Lote" ("tipo") VALUES
('Perecível'),
('Não Perecível'),
('Bebidas'),
('Limpeza'),
('Higiene');

-- ProdutoLote

-- Compra 

-- Requisicao
INSERT INTO "Requisicao" ("descricao", "dataLancamento", "dataConfirmacao", "status", "pendente", "aprovado", "numLote", "cpfEstoquista", "cpfOperador") VALUES
('Requisição de ingredientes', '2024-08-25', '2024-08-26', 'aprovado', false, true, 1, '56789012345', '12345678901'),
('Requisição de bebidas', '2024-08-26', NULL, 'pendente', true, false, 2, '45678901234', '23456789012'),
('Requisição de produtos de limpeza', '2024-08-27', '2024-08-28', 'aprovado', false, true, 4, '34567890123', '34567890123'),
('Requisição de itens de higiene', '2024-08-28', NULL, 'pendente', true, false, 5, '23456789012', '45678901234'),
('Requisição de carnes', '2024-08-29', '2024-08-30', 'aprovado', false, true, 1, '12345678901', '56789012345');

-- Saida
INSERT INTO "Saida" ("descricao", "dataLancamento", "dataConfirmacao", "status", "pendente", "aprovado", "numLote", "cpfEstoquista", "cpfOperador", "codRequisicao") VALUES
('Saída de ingredientes para preparo', '2024-08-20', '2024-08-21', 'aprovado', false, true, 1, '12345678901', '23456789012', 1),
('Saída de bebidas para reposição', '2024-08-22', '2024-08-23', 'aprovado', false, true, 2, '23456789012', '34567890123', 2),
('Saída de produtos de limpeza', '2024-08-24', '2024-08-25', 'aprovado', false, true, 4, '34567890123', '45678901234', 3),
('Saída de itens de higiene', '2024-08-26', '2024-08-27', 'aprovado', false, true, 5, '45678901234', '56789012345', 4),
('Saída de carnes para preparo', '2024-08-28', '2024-08-29', 'aprovado', false, true, 1, '56789012345', '12345678901', 5);

-- Entrada

-- Ajuste