import requests
import csv
from bs4 import BeautifulSoup
from urllib.parse import urljoin  # Добавляем для работы с относительными URL

# URL страницы, которую нужно парсить
base_url = "https://kingfisher.kz/"  # Базовый URL

# Отправка GET-запроса для получения страницы
response = requests.get(base_url)
soup = BeautifulSoup(response.content, "html.parser")

# Функция для извлечения категорий
def extract_categories(soup):
    categories = []
    # Поиск всех категорий
    category_elements = soup.find_all("li", class_="dropmenu")

    for category in category_elements:
        category_name = category.find("span").get_text(strip=True)
        subcategories = extract_subcategories(category)

        categories.append({
            "category": category_name,
            "subcategories": subcategories
        })

    return categories

# Функция для извлечения подкатегорий
def extract_subcategories(category_element):
    subcategories = []
    # Поиск всех подкатегорий в каждой категории
    subcategory_elements = category_element.find("ul", class_="submenu").find_all("li")

    for subcategory in subcategory_elements:
        # Проверяем, что тег <a> существует
        link = subcategory.find("a")
        if link:
            subcategory_name = link.get_text(strip=True)
            subcategory_url = link.get("href")
            full_url = urljoin(base_url, subcategory_url)  # Создаем полный URL для подкатегории
            subcategories.append({
                "name": subcategory_name,
                "url": full_url
            })

    return subcategories

# Функция для извлечения продуктов из подкатегории
def extract_products(subcategory_url):
    products = []
    response = requests.get(subcategory_url)
    soup = BeautifulSoup(response.content, "html.parser")

    product_elements = soup.find_all("span", class_="wrapperPad")

    for product in product_elements:
        product_name = product.find("a", class_="title").get_text(strip=True) if product.find("a", class_="title") else "Без названия продукта"
        product_description = product.find("span", class_="descript").get_text(strip=True) if product.find("span", class_="descript") else "Нет описания"
        product_price = product.find("span", class_="new").get_text(strip=True) if product.find("span", class_="new") else "Цена не указана"

        products.append({
            "product_name": product_name,
            "description": product_description,
            "price": product_price
        })

    return products

# Функция для записи данных в CSV файл
def write_to_csv(data, filename="products.csv"):
    # Определяем заголовки для CSV файла
    headers = ["Категория", "Подкатегория", "Продукт", "Описание", "Цена"]

    # Записываем данные в CSV файл
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)

        # Записываем заголовок
        writer.writeheader()

        # Записываем строки данных
        for row in data:
            writer.writerow(row)

# Сбор всех данных
all_data = []

# Основной процесс парсинга
categories = extract_categories(soup)

# Для каждого подкатегории получаем список продуктов
for category in categories:
    for subcategory in category["subcategories"]:
        subcategory_url = subcategory["url"]  # Теперь это полный URL
        print(f"Обработка подкатегории: {subcategory['name']} с URL: {subcategory_url}")
        products = extract_products(subcategory_url)

        # Собираем данные для записи
        for product in products:
            all_data.append({
                "Категория": category["category"],
                "Подкатегория": subcategory["name"],
                "Продукт": product["product_name"],
                "Описание": product["description"],
                "Цена": product["price"]
            })

# Запись данных в CSV файл
write_to_csv(all_data)
