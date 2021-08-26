-- Departamento
CREATE TABLE Departamento
(
    id_departamento INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(160) NOT NULL
);


-- Colaborador

CREATE TABLE Colaborador
(
    id_colaborador INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(160)  NOT NULL,
    id_departamento INTEGER  NOT NULL,

    FOREIGN KEY (id_departamento) REFERENCES Departamento(id_departamento) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
);


-- Dependente

CREATE TABLE Dependente
(
    id_dependente INT AUTO_INCREMENT PRIMARY KEY,
    nome NVARCHAR(160)  NOT NULL,
    id_colaborador INTEGER  NOT NULL,

    FOREIGN KEY (id_colaborador) REFERENCES Colaborador (id_colaborador) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
);