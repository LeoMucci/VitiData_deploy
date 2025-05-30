FROM python:3.11-slim

# Evita prompts interativos
ENV DEBIAN_FRONTEND=noninteractive

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    chromium-driver \
    chromium \
    curl \
    unzip \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# Define diretório de trabalho
WORKDIR /app

# Copia todos os arquivos do projeto
COPY . .

# Instala dependências Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Define variáveis para o Selenium funcionar corretamente
ENV PATH="/usr/lib/chromium:/usr/bin:$PATH"
ENV CHROME_BIN="/usr/bin/chromium"
ENV CHROMEDRIVER_PATH="/usr/bin/chromedriver"

# Porta usada pelo Flask
EXPOSE 5000

# Comando para iniciar o app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
