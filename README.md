
# Sobre o Desevolvimento e Execução do Projeto

## Resumo:

As APIs REST são construídas usando o framework Flask e podem ser utilizadas com os Bancos de Dados MySQL ou SqlLite. 
Os contêineres do Docker são usados ​​para o ambiente de desenvolvimento.

### Estrutura do projeto

```bash
Flask-Nginx-DockerCompose-Sqlalchemy-Sqlite-MySQL /
├── api
│   ├── controllers
│   │   ├── __init__.py
│   │   ├── colaboradores_controller.py.py
│   │   ├── departamentos_controller.py
│   │   └── dependentes_controller.py
│   ├── extensions
│   │   ├── __init__.py
│   │   ├── database_enum.py.py
│   │   └── utils.py
│   ├── infra
│   │   ├── config-database
│   │   │   ├── __init__.py
│   │   │   └── db.py
│   │   └── __init__.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── colaboradores_model.py.py
│   │   ├── departamentos_model.py
│   │   └── dependentes_model.py
│   ├── schemas
│   │   ├── __init__.py
│   │   ├── colaboradores_schema.py.py
│   │   ├── departamentos_schema.py
│   │   └── dependentes_schema.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── colaboradores_service.py.py
│   │   ├── departamentos_service.py
│   │   └── dependentes_service.py
│   ├── __init__.py
│   ├── .dockerignore
│   ├── app.ini
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── db
│   ├── 1.0
│   │   ├── modelo-dados
│   │   └── scripts-sql
├── nginx
│   ├── Dockerfile
│   └── nginx.conf
├── .gitignore
├── docker-compose.yml
└── README.md
```

### Requisitos iniciais 

- Instalar Docker
- Instalar Docker Compose

Clone o projeto usando o comando:
```bash
git clone https://github.com/githubgoncalves/Flask-Nginx-DockerCompose-Sqlalchemy-Sqlite-MySQL.git
```

### Como iniciar o aplicativo (usando Docker Compose)

Vá para o diretório do projeto:
```bash
cd Flask-Nginx-DockerCompose-Sqlalchemy-Sqlite-MySQL
```
Execute o aplicativo com o seguinte comando para executar os containers docker:
```bash
docker-compose up -d 
```


### Documentação Swagger - TODO - (Ajustando Endpoint do Swagger)

 ```bash
http://localhost:5000/docs
```

### Endpoint API Listar Colaboradores

 ```bash
http://localhost:5000/api/colaboradores/listar
```

### Endpoint API Listar Departamentos

 ```bash
http://localhost:5000/api/departamentos/listar
```

### Endpoint API Listar Dependentes

 ```bash
http://localhost:5000/api/dependentes/listar
```

### Endpoints API

```bash
http://localhost:5000/api/colaboradores/
http://localhost:5000/api/dependentes/
http://localhost:5000/api/departamentos/
```

# Base de Dados

Na pasta Flask-Nginx-DockerCompose-Sqlalchemy-Sqlite-MySQL/db tem o modelo de dados e o script para criação das tabelas no MySQL. 

## SQL LITE

A base de dados do SqlLite é criada automaticamente ao iniciar o projeto.

## Acessando URL Adminer do MySQL 

http://127.0.0.1:8080/

- server: mysql-db
- usuario: root
- senha: api
- base: api

## Scripts - MySQL

Executar na base do MySQL via Adminier os scripts de criação das tabelas (Flask-Nginx-DockerCompose-Sqlalchemy-Sqlite-MySQL/db/scripts-sql.sql)

**Contato com [DANIEL GONÇALVES](danielgoncalves.info@gmail.com)!**


