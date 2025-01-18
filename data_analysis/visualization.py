import matplotlib.pyplot as plt
import pandas as pd
import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="kingfisher_db",
    user="postgres",
    password="",
    host="localhost",
    port="5433"
)

# Получение данных из базы данных
df = pd.read_sql_query("SELECT * FROM products", conn)

# Построение гистограммы цен
plt.figure(figsize=(10, 6))
plt.hist(df['price'], bins=30, edgecolor='black')
plt.title('Распределение цен продуктов')
plt.xlabel('Цена')
plt.ylabel('Частота')
plt.show()
