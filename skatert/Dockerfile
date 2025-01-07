# Базовый образ Python
FROM python:3.11-slim

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y libpq-dev gcc

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt /app/

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . /app/

# Собираем статические файлы
RUN python manage.py collectstatic --noinput

# Указываем порт для работы приложения
EXPOSE 8000

# Команда запуска Django-приложения
CMD ["gunicorn", "skatert.wsgi:application", "--bind", "0.0.0.0:8000"]
