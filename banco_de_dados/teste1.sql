CREATE DATABASE IF NOT EXISTS loja;
USE loja;

CREATE TABLE clientes(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR (100) NOT NULL,
    idade INT
);

CREATE TABLE produtos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    estoque INT NOT NULL
);

INSERT INTO clientes (nome, email, idade)
VALUES
('João', 'joao@email.com', 20),
('Maria', 'maria@email.com', 25),
('Pedro', 'pedro@email.com', 31);

INSERT INTO produtos (nome, preco, estoque)
VALUES
('Mouse', 50.00, 10),
('Teclado', 120.00, 5),
('Monitor', 900.00, 3);