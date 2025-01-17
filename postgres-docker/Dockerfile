# Используем официальный образ PostgreSQL
FROM postgres:13

# Устанавливаем переменные окружения для базы данных
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=dimashprpr
ENV POSTGRES_DB=kingfisher_db

# Копируем скрипт инициализации
COPY init.sql /docker-entrypoint-initdb.d/

# Указываем порт PostgreSQL
EXPOSE 5432
