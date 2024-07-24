# Projeto de Processamento de Dados e Integração com DBT

## Visão Geral

Este projeto visa construir uma pipeline de dados completa, seguindo as seguintes etapas:

1. **Extração e Processamento de Dados**
   - Os dados são extraídos e inicialmente salvos em arquivos CSV.
   - A biblioteca Polars é utilizada para o processamento e tratamento dos dados.

2. **Carregamento de Dados**
   - Os dados processados são carregados em uma tabela no banco de dados PostgreSQL.

3. **Criação de Tabela Derivada**
   - Uma tabela derivada é criada usando DBT.


## Pré-requisitos

- Python (3.11.9)
- Docker
- Docker Compose

## Começando

### Passo 1: Configurar Variáveis de Ambiente

Atualize o arquivo `.env` no diretório raiz do projeto para configurar suas variáveis de ambiente:

```
   # Postgres keys
   HOST=seuhost
   USER=seuusuario
   PASSWORD=suasenha
   DATABASE2=seubanco
   PORT=5432

   # Prefect keys
   PREFECT_API_DATABASE_CONNECTION_URL2=postgresql+asyncpg://seuusuario:suasenha@prefect-postgres:5432/prefect
   APP_DATABASE_CONNECTION_URL=postgresql+asyncpg://seuusuario:suasenha@prefect-postgres:5432/seubanco
   PREFECT_API_URL2=http://host.docker.internal:4200/api

   # Flags
   UPDATE_URLS=False (Se não possuir os url's dos últimos meses, mude esta flag para True )
```

### Passo 2: Construir e Executar os Containers Docker e Prefect Server

Execute o seguinte comando para construir e iniciar os containers Docker e Prefect Server:

```sh
docker-compose up --build
```

### Passo 3: Acessar o Servidor Prefect

Abra o seu navegador e vá para http://localhost:4200 para acessar a interface do Prefect Server.

### Passo 4: Verificar Dados no PostgreSQL

Para conectar-se ao banco de dados PostgreSQL dentro do container, execute:

```sh
docker exec -it prefect-postgres psql -U seuusuario 
```

Para listar todos os bancos de dados:

```sh
\l
```

## Serviços

- **Postgres**: Banco de dados PostgreSQL para armazenar dados processados.
- **Prefect**: Servidor Prefect para orquestrar e gerenciar fluxos de trabalho de dados.
- **App**: Aplicação Python para fazer download, transformar e carregar dados.
- **DBT**: Data Build Tool para transformar dados após o carregamento.