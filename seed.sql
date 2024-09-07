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
('56789012345', 'M', 11943210987, 'José Fernandes', '2022-09-30', 'E'),
('78901234568', 'F', 11921098766, 'Renata Costa', '2022-12-27', 'E'),
('89012345679', 'M', 11910987655, 'Daniel Alves', '2023-08-19', 'O'),
('90123456780', 'F', 11909876544, 'Vanessa Teixeira', '2022-07-04', 'G');

-- Categoria
INSERT INTO "Categoria" ("nome") VALUES
('Carnes'),
('Bebidas'),
('Laticínios'),
('Hortifrúti'),
('Grãos'),
('Pães e Bolos'),
('Doces e Sobremesas'),
('Enlatados'),
('Temperos'),
('Frios e Embutidos');

-- Produto
INSERT INTO "Produto" ("unidade", "quantidade", "nome", "descricao", "codCategoria") VALUES
-- Carnes (Categoria 1)
('kg', 1, 'Filé Mignon', 'Carne de alta qualidade', 1),
('kg', 1, 'Picanha', 'Corte nobre de carne bovina', 1),
('kg', 1, 'Frango Inteiro', 'Frango inteiro resfriado', 1),
('kg', 1, 'Costela Suína', 'Carne suína com osso', 1),
('kg', 1, 'Alcatra', 'Carne bovina de primeira', 1),

-- Bebidas (Categoria 2)
('ml', 500, 'Água Mineral', 'Garrafa de 500ml', 2),
('ml', 350, 'Refrigerante', 'Lata de 350ml', 2),
('ml', 350, 'Cerveja', 'Lata de 350ml', 2),
('ml', 750 , 'Vinho Tinto', 'Garrafa de 750ml', 2),
('L', 1 , 'Suco de Laranja', 'Caixa de 1L', 2),

-- Laticínios (Categoria 3)
('L', 1, 'Leite Integral', 'Leite integral pasteurizado', 3),
('g', 200, 'Queijo Mussarela', 'Queijo mussarela fatiado', 3),
('g', 200, 'Iogurte Natural', 'Iogurte natural sem açúcar', 3),
('g', 200, 'Manteiga', 'Manteiga com sal', 3),
('g', 400, 'Requeijão', 'Requeijão cremoso', 3),

-- Hortifrúti (Categoria 4)
('kg', 1, 'Maçã', 'Maçã vermelha', 4),
('kg', 1, 'Banana', 'Banana prata', 4),
('kg', 1, 'Tomate', 'Tomate italiano', 4),
('kg', 1, 'Alface', 'Alface crespa', 4),
('kg', 1, 'Batata', 'Batata inglesa', 4),

-- Grãos (Categoria 5)
('kg', 1, 'Arroz Branco', 'Arroz branco tipo 1', 5),
('kg', 1, 'Feijão Preto', 'Feijão preto', 5),
('g', 500, 'Lentilha', 'Lentilha seca', 5),
('g', 500, 'Grão de Bico', 'Grão de bico', 5),
('g', 500, 'Quinoa', 'Quinoa em grãos', 5),

-- Pães e Bolos (Categoria 6)
('g', 500, 'Pão de Forma', 'Pão de forma integral', 6),
('g', 300, 'Baguete', 'Pão baguete', 6),
('g', 400, 'Bolo de Chocolate', 'Bolo de chocolate caseiro', 6),
('g', 400, 'Croissant', 'Croissant de manteiga', 6),
('g', 400, 'Pão de Queijo', 'Pão de queijo tradicional', 6),

-- Doces e Sobremesas (Categoria 7)
('g', 200, 'Chocolate ao Leite', 'Chocolate ao leite', 7),
('g', 250, 'Doce de Leite', 'Doce de leite cremoso', 7),
('g', 200, 'Brigadeiro', 'Brigadeiro tradicional', 7),
('g', 100, 'Goiabada', 'Goiabada em pedaços', 7),
('g', 250, 'Pudim', 'Pudim de leite condensado', 7),

-- Enlatados (Categoria 8)
('g', 400, 'Milho em Conserva', 'Milho verde em conserva', 8),
('g', 400, 'Ervilha em Conserva', 'Ervilha verde em conserva', 8),
('g', 400, 'Sardinha em Óleo', 'Sardinha em óleo vegetal', 8),
('g', 400, 'Atum em Água', 'Atum em conserva', 8),
('g', 300, 'Tomate Pelado', 'Tomate pelado em lata', 8),

-- Temperos (Categoria 9)
('g', 100, 'Sal', 'Sal refinado', 9),
('g', 50, 'Pimenta do Reino', 'Pimenta do reino moída', 9),
('g', 50, 'Orégano', 'Orégano seco', 9),
('g', 50, 'Açafrão', 'Açafrão da terra', 9),
('g', 50, 'Manjericão', 'Manjericão desidratado', 9),

-- Frios e Embutidos (Categoria 10)
('g', 200, 'Presunto', 'Presunto fatiado', 10),
('g', 200, 'Mortadela', 'Mortadela fatiada', 10),
('g', 150, 'Salame', 'Salame italiano', 10),
('g', 200, 'Peito de Peru', 'Peito de peru fatiado', 10),
('g', 300, 'Salsicha', 'Salsicha tipo viena', 10);

-- Fornecedor
INSERT INTO "Fornecedor" ("cnpjFornecedor", "endereco", "razao", "nome", "telefone") VALUES
('12345678000199', 'Rua A, 123', 'Fornecedor A Ltda', 'Fornecedor A', 1234567890),
('23456789000188', 'Rua B, 456', 'Fornecedor B Ltda', 'Fornecedor B', 2345678901),
('34567890000177', 'Rua C, 789', 'Fornecedor C Ltda', 'Fornecedor C', 3456789012),
('45678901000166', 'Rua D, 101', 'Fornecedor D Ltda', 'Fornecedor D', 4567890123),
('56789012000155', 'Rua E, 202', 'Fornecedor E Ltda', 'Fornecedor E', 5678901234),

('67890123000144', 'Rua F, 303', 'Fornecedor F Ltda', 'Fornecedor F', 6789012345),
('78901234000133', 'Rua G, 404', 'Fornecedor G Ltda', 'Fornecedor G', 7890123456),
('89012345000122', 'Rua H, 505', 'Fornecedor H Ltda', 'Fornecedor H', 8901234567),
('90123456000111', 'Rua I, 606', 'Fornecedor I Ltda', 'Fornecedor I', 9012345678),
('01234567000100', 'Rua J, 707', 'Fornecedor J Ltda', 'Fornecedor J', 1234567809);

-- Restaurante
INSERT INTO "Restaurante" ("cnpjRestaurante", "endereco", "razao", "nome", "telefone", "cnpjMatriz", "cpfGerente") VALUES
('98765432000199', 'Avenida X, 987', 'Restaurante X Ltda', 'Restaurante X', 9876543210, NULL, '12345678901'),
('87654321000188', 'Avenida Y, 876', 'Restaurante Y Ltda', 'Restaurante Y', 8765432109, '98765432000199', '67890123456'),
('76543210000177', 'Avenida Z, 765', 'Restaurante Z Ltda', 'Restaurante Z', 7654321098, '98765432000199', '78901234567'),
('65432100000166', 'Rua W, 654', 'Restaurante W Ltda', 'Restaurante W', 6543210987, '87654321000188', '89012345678'),
('54321000000155', 'Rua V, 543', 'Restaurante V Ltda', 'Restaurante V', 5432109876, NULL, '90123456789');

UPDATE "Funcionario" SET "cnpjRestaurante" = '98765432000199';

-- Cotacao
INSERT INTO "Cotacao" ("valor", "codProduto", "cnpjFornecedor") VALUES
(150.00, 1, '12345678000199'),  
(120.00, 2, '12345678000199'),   
(25.00, 3, '12345678000199'),    
(70.00, 4, '12345678000199'),    
(95.00, 5, '12345678000199'),    

(155.00, 1, '23456789000188'),  
(160.00, 2, '23456789000188'),   
(30.00, 3, '23456789000188'),    
(60.00, 4, '23456789000188'),    
(109.00, 5, '23456789000188'),  

(125.00, 1, '34567890000177'),  
(190.00, 2, '34567890000177'),   
(38.00, 3,  '34567890000177'),    
(71.00, 4,  '34567890000177'),    
(97.00, 5, '34567890000177'),  

(2.00, 6, '23456789000188'),  
(4.50, 7, '23456789000188'),    
(5.50, 8, '23456789000188'),    
(25.00, 9, '23456789000188'),   
(8.00, 10, '23456789000188'),  

(6.00, 11, '34567890000177'),   
(8.00, 12, '34567890000177'),  
(4.00, 13, '34567890000177'),   
(9.00, 14, '34567890000177'),   
(7.00, 15, '34567890000177'),  

(4.50, 16, '45678901000166'),
(3.20, 17, '45678901000166'),
(5.80, 18, '45678901000166'),
(2.30, 19, '45678901000166'),
(3.50, 20, '45678901000166'),

(7.00,  21, '56789012000155'),
(6.00,  22, '56789012000155'),
(12.00, 23, '56789012000155'),
(10.00, 24, '56789012000155'),
(15.00, 25, '56789012000155'),

(5.50, 26, '67890123000144'),
(3.20, 27, '67890123000144'),
(15.00, 28, '67890123000144'),
(4.00, 29, '67890123000144'),
(6.00, 30, '67890123000144'), 

(4.50, 31, '78901234000133'),
(6.00, 32, '78901234000133'),
(5.00, 33, '78901234000133'),
(3.50, 34, '78901234000133'),
(7.00, 35, '78901234000133'),

(2.50, 36, '89012345000122'),
(3.00, 37, '89012345000122'),
(4.00, 38, '89012345000122'),
(5.00, 39, '89012345000122'),
(3.20, 40, '89012345000122'),

(1.00, 41, '90123456000111'),
(2.00, 42, '90123456000111'),
(2.50, 43, '90123456000111'),
(3.00, 44, '90123456000111'),
(2.20, 45, '90123456000111'),

(12.00, 46, '01234567000100'),
(10.00, 47, '01234567000100'),
(15.00, 48, '01234567000100'),
(13.00, 49, '01234567000100'),
(9.00, 50, '01234567000100');

-- Estoque
INSERT INTO "Estoque" ("codEstoque","nome", "cnpjRestaurante") VALUES
(1,'Estoque de Carnes', '98765432000199'),
(2,'Estoque de Bebidas', '98765432000199'),
(3,'Estoque de Laticínios Central', '98765432000199'),
(4,'Estoque de Hortifrúti', '98765432000199'),
(5,'Estoque de Enlatados', '98765432000199');

-- ProdutoEstoque
INSERT INTO "ProdutoEstoque" ("codProduto", "codEstoque", "estoqueMax", "estoqueMin", "estoqueAtual", "estoqueDisp", "ultimoInv") VALUES
(1, 1, 100, 20, 0, 0, '2024-09-01'),
(2, 1, 200, 50, 0, 0, '2024-09-01'),
(3, 1, 300, 100, 0, 0, '2024-09-01'),
(4, 1, 150, 30, 0, 0, '2024-09-01'),
(5, 1, 400, 150, 0, 0, '2024-09-01');

-- Lote
INSERT INTO "Lote" ("tipo") VALUES
('entrada'),
('entrada'),
('entrada'),
('entrada'),
('entrada'),
('saida'),
('saida'),
('saida'),
('saida'),
('saida');

-- ProdutoLote
INSERT INTO "ProdutoLote" ("codProduto", "codEstoque", "numLote", "quantidade") VALUES
--entradas lote de carnes
(1, 1, 1, 100),
(2, 1, 1, 50),
(3, 1, 1, 50),
(4, 1, 1, 50),
(5, 1, 1, 50),

(2, 1, 2, 50),
(3, 1, 3, 50),
(4, 1, 4, 50),
(5, 1, 5, 50),

--requisicoes lote de carnes
(1, 1, 6, 10),
(2, 1, 6, 10),
(3, 1, 6, 10),
(4, 1, 6, 10),
(5, 1, 6, 10),

(2, 1, 7, 10),
(3, 1, 8, 20),
(4, 1, 9, 30),
(5, 1, 10, 40);


-- Entrada
INSERT INTO "Entrada" ("descricao", "dataLancamento", "numLote", "cpfEstoquista", "cpfOperador","codEstoque","pendente","aprovado") VALUES
('Entrada de carnes', '2024-08-20', 1, '12345678901', '23456789012',1,false,true),
('Entrada de bebidas', '2024-08-22', 2, '23456789012', '34567890123',1,false,true),
('Entrada de produtos de limpeza', '2024-08-24', 3, '34567890123', '45678901234',1,false,true),
('Entrada de itens de higiene', '2024-08-26', 4, '45678901234', '56789012345',1,false,true),
('Entrada de ingredientes perecíveis', '2024-08-28', 5, '56789012345', '12345678901',1,false,true);

-- Compra 
-- INSERT INTO "Compra" ("codOperacao", "cnpjFornecedor", "cnpjRestaurante", "notaFiscal", "data", "quantidade") VALUES
-- (1, '12345678000199', '98765432000199', decode('DEADBEEF', 'hex'), '2024-08-20', 100),
-- (2, '23456789000188', '98765432000199', decode('CAFEBABE', 'hex'), '2024-08-22', 200),
-- (3, '34567890000177', '98765432000199', decode('BEEFFACE', 'hex'), '2024-08-24', 150),
-- (4, '45678901000166', '98765432000199', decode('FEEDFACE', 'hex'), '2024-08-26', 300),
-- (5, '56789012000155', '98765432000199', decode('BADF00D', 'hex'), '2024-08-28', 250);


-- Saida
INSERT INTO "Saida" ("descricao","dataLancamento",  "numLote", "cpfEstoquista", "cpfOperador", "codEstoque","pendente","aprovado") VALUES
('Saída de carnes', '2024-08-25',  6, '56789012345', '12345678901',1,true,false),
('Saída de bebidas', '2024-08-26', 7, '45678901234', '23456789012',1,true,false),
('Saída de produtos de limpeza', '2024-08-27',  8, '34567890123', '34567890123',1,true,false),
('Saída de itens de higiene', '2024-08-28',  9, '23456789012', '45678901234',1,true,false),
('Saída de ingredientes', '2024-08-29',  10, '12345678901', '56789012345',1,true,false);

-- Inventario
INSERT INTO "Inventario" ("codProduto", "codEstoque", "data", "contagem", "cpfOperador") VALUES
(1, 1, '2024-08-01', 45, '56789012345'),
(2, 1, '2024-08-02', 115, '45678901234'),
(3, 1, '2024-08-03', 240, '56789012345'),
(4, 1, '2024-08-04', 75, '45678901234'),
(5, 1, '2024-08-05', 330, '56789012345');
