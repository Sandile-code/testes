CREATE DATABASE escola;
USE escola;

CREATE TABLE alunos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    idade INT,
    curso VARCHAR(50)
);

INSERT INTO alunos (nome, idade, curso)
VALUES
("João", 20, "Informática"),
("Maria", 21, "Administração"),
("Pedro", 19, "Direito");

SELECT * FROM alunos;

UPDATE alunos
SET idade = 22
WHERE id = 2;

SELECT * FROM alunos
WHERE idade >= 20
ORDER BY nome;