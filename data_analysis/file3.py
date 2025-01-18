import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="kingfisher_db",  # Имя вашей базы данных
    user="postgres",             # Имя пользователя
    password="",  # Ваш пароль
    host="localhost",          # Хост
    port="5433"                # Порт
)

# Загружаем данные из базы данных в pandas DataFrame
df = pd.read_sql_query("SELECT * FROM products", conn)

# Закрытие соединения с базой данных
conn.close()

# Преобразуем цену в числовой формат, если это необходимо
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Проводим базовый анализ данных
print("Основные статистические характеристики:")
print(df.describe())

# Проверка на пропущенные значения
print("\nПропущенные значения:")
print(df.isnull().sum())

# Анализ распределения цен
plt.figure(figsize=(10, 6))
sns.histplot(df['price'], bins=30, kde=True)
plt.title('Распределение цен')
plt.xlabel('Цена')
plt.ylabel('Частота')
plt.show()

# Анализ средней цены по категориям
category_avg_price = df.groupby('category')['price'].mean().sort_values(ascending=False)
plt.figure(figsize=(12, 8))
category_avg_price.plot(kind='bar', color='skyblue')
plt.title('Средняя цена по категориям')
plt.xlabel('Категория')
plt.ylabel('Средняя цена')
plt.xticks(rotation=90)
plt.show()

# Топ-5 самых дорогих продуктов
top_5_expensive = df[['product_name', 'price']].sort_values(by='price', ascending=False).head(5)
print("\nТоп-5 самых дорогих продуктов:")
print(top_5_expensive)
