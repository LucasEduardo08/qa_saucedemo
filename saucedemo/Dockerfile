# Imagem oficial do Playwright com Python e browsers, irá importá-la
FROM mcr.microsoft.com/playwright/python:v1.62.0-noble

# Define o diretório de trabalho dentro do container, tipo um cd app/
WORKDIR /app

# Copia primeiro os arquivos de dependências
COPY pyproject.toml poetry.lock ./

# Instala Poetry
RUN pip install poetry

# Não cria virtualenv dentro do container
RUN poetry config virtualenvs.create false

# Instala as dependências do projeto
RUN poetry install --no-root

# Copia o restante do projeto
COPY . .

# Comando padrão do container, comando: poetry run pytest
CMD ["poetry", "run", "pytest"]