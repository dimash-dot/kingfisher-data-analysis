Kingfisher Data Analysis

Цель проекта:
Парсинг данных с сайта Kingfisher.kz, их сохранение в PostgreSQL и анализ данных для визуализации и выводов.

# Анализ данных с Kingfisher.kz
my_project/
├── parsing_code/
│   ├── scraper.py           # Скрипт для парсинга данных с сайта
│     
├── docker_sql/
│   ├── docker-compose.yml   # Docker Compose файл для запуска PostgreSQL
│   ├── init.sql             # SQL-скрипт для создания базы данных и таблиц
├── data_analysis/
│   ├── analysis.py          # Скрипт для анализа данных и визуализации
│   ├── visualization.py     # Скрипт для построения графиков
│  
├── README.md                # Инструкция по запуску

## Структура репозитория
- `parsing_code/`: Скрипты для парсинга данных с сайта Kingfisher.kz.
- `docker_sql/`: Docker-скрипты для развертывания PostgreSQL.
- `data_analysis/`: Скрипты для анализа и визуализации данных.

Установка

1. Клонируйте репозиторий:

git clone https://github.com/dimash-dot/kingfisher-data-analysis.git
cd kingfisher-data-analysis

2. Установите необходимые библиотеки:

pip install -r requirements.txt

3. Разверните PostgreSQL в Docker:

cd docker_sql
docker-compose up -d

Примечание о работе с Docker
При выполнении данного задания я впервые работал с Docker, поэтому возникли некоторые трудности с полной интеграцией системы для автоматической передачи данных в базу данных через контейнер. В результате я решил упростить процесс, чтобы гарантировать стабильность работы. Сейчас данные сразу передаются в базу данных через Python-скрипт, минуя автоматизированную загрузку из Docker.

⚠️ Примечание: Несмотря на это, база данных PostgreSQL успешно разворачивается в Docker, а данные из CSV файла загружаются в таблицы через скрипт.

Этот проект — мой первый опыт работы с Docker, и я надеюсь улучшить свои навыки в будущих задачах, добавив более гибкие и автоматизированные решения.

4. Запустите скрипт для парсинга данных:

python parsing_code/scraper.py

5. Загрузите данные в PostgreSQL:

python parsing_code/load_to_db.py

6. Анализируйте и визуализируйте результаты:

python data_analysis/analysis.py

Примечания

Скрипты писаны на Python 3.10+.

DB_NAME=kingfisher_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5433
здесь нужно написать свои данные 