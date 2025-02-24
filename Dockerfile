# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Устанавливаем необходимые пакеты для Allure
RUN apt-get update && apt-get install -y \
    default-jre \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Allure
RUN wget https://github.com/allure-framework/allure2/releases/download/2.22.0/allure-2.22.0.zip \
    && unzip allure-2.22.0.zip -d /opt/ \
    && ln -s /opt/allure-2.22.0/bin/allure /usr/bin/allure \
    && rm allure-2.22.0.zip

# Копируем файл с зависимостями
COPY requirements.txt .

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта
COPY . .

# Команда для запуска тестов и генерации отчета Allure
CMD ["sh", "-c", "pytest --alluredir=./allure-results && allure serve ./allure-results"]