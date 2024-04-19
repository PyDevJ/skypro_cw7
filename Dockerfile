# Используем базовый образ Python
FROM python:3

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости и код приложения
COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Команда для запуска Django-сервера
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]