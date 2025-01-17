import psycopg2
import pandas as pd
import chardet

cur = None
conn = None

try:
    # Подключение к базе данных PostgreSQL
    conn = psycopg2.connect(
        dbname="kingfisher_db",  # Убедитесь, что база данных существует
        user="postgres",
        password="dimashprpr",
        host="localhost",  # Убедитесь, что контейнер доступен по этому хосту
        port="5433"  # Используем порт 5433 для подключения к Docker контейнеру
    )

    cur = conn.cursor()

    # Определение кодировки CSV файла
    with open("C:/Users/Dimash/IdeaProjects/untitled2/products.csv", 'rb') as f:
        result = chardet.detect(f.read())
        print(f"Определенная кодировка файла: {result['encoding']}")

    # Загрузка данных из CSV файла с явной кодировкой
    try:
        df = pd.read_csv("C:/Users/Dimash/IdeaProjects/untitled2/products.csv", encoding=result['encoding'])
    except UnicodeDecodeError:
        df = pd.read_csv("C:/Users/Dimash/IdeaProjects/untitled2/products.csv", encoding="latin1")

    # Отладка: выводим первые 5 строк из CSV для проверки
    print(df.head())

    # Преобразуем цену: удаляем пробелы и символы (например, "Т") и конвертируем в float
    df['Цена'] = df['Цена'].replace({' Т': '', ' ': ''}, regex=True).astype(float)

    # Преобразуем данные в формат, который можно вставить в таблицу
    for index, row in df.iterrows():
        try:
            cur.execute("""
                INSERT INTO products (category, subcategory, product_name, description, price)
                VALUES (%s, %s, %s, %s, %s)
            """, (row['Категория'], row['Подкатегория'], row['Продукт'], row['Описание'], row['Цена']))
            print(f"Загружена строка {index + 1}")
        except Exception as e:
            print(f"Ошибка при загрузке строки {index + 1}: {e}")

    # Сохраняем изменения
    conn.commit()

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    # Проверка существования переменных перед их закрытием
    if cur:
        cur.close()
    if conn:
        conn.close()

print("Данные успешно загружены в базу данных.")
