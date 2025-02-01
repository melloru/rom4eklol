# Используем официальный образ Python в качестве базового
FROM python:3.13-slim

# Устанавливаем рабочую директорию
WORKDIR /application

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry

# Копируем файлы конфигурации Poetry в контейнер
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости с помощью Poetry
RUN poetry install --no-root

# Копируем все файлы приложения в контейнер
COPY . .

# Открываем порт, на котором будет работать приложение
EXPOSE 8000

# Команда для запуска приложения
CMD ["poetry", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]