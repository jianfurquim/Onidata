# Usando a imagem base do Python
FROM python:3.10

# Definindo o diretório de trabalho no container
WORKDIR /code

# Copiando o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt /code/

# Instalando as dependências do projeto
RUN pip install -r requirements.txt

# Copiando todo o código para o diretório de trabalho
COPY . /code/

# Comando padrão a ser executado ao iniciar o container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]