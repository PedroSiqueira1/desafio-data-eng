# Imagem base do Python
FROM python:3.9

# Diretório de trabalho no contêiner
WORKDIR /app

# Arquivos de requisitos para o contêiner
COPY requirements.txt .

# Dependências
RUN pip install --no-cache-dir -r requirements.txt

# Código para o contêiner
COPY src/ /app/
COPY urls.csv /app/

# Rodar a aplicação
CMD ["python", "main.py"]