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

- Docker
- Docker Compose

## Começando

### Passo 1: Configurar Variáveis de Ambiente

Crie um arquivo `.env` no diretório raiz do projeto e adicione as seguintes variáveis de ambiente:

```
    HOST=seu_host
    USER=seu_usuário
    PASSWORD=sua_senha
    DATABASE=seu_database
    PORT=sua_porta
    DIALECT=postgresql+psycopg2 (Não modifique esta variável)
```

### Passo 2: Inicializar o Banco de Dados

Certifique-se de que o arquivo `init.sql` está configurado corretamente para criar o banco de dados e as tabelas necessárias.

### Passo 3: Construir e Executar os Containers Docker

Execute o seguinte comando para construir e iniciar os containers Docker:

```sh
docker-compose up --build
```

### Passo 4: Acessar o Servidor Prefect

Abra o seu navegador e vá para http://localhost:4200 para acessar a interface do servidor Prefect.

### Passo 5: Verificar Dados no PostgreSQL

Para conectar-se ao banco de dados PostgreSQL dentro do container, execute:

```sh
docker exec -it prefect-postgres psql -U seu_usuario_postgres -d orcamento_contratos
```

Para listar todos os bancos de dados:

```sh
\l
```

Para conectar-se ao banco de dados orcamento_contratos:

```sh
\c orcamento_contratos
```

## Serviços

- **Postgres**: Banco de dados PostgreSQL para armazenar dados processados.
- **Prefect**: Servidor Prefect para orquestrar e gerenciar fluxos de trabalho de dados.
- **App**: Aplicação Python para fazer download, transformar e carregar dados.
- **DBT**: Data Build Tool para transformar dados após o carregamento.