import sqlite3
import requests
from bs4 import BeautifulSoup
import datetime

def create_tables():
    conn = sqlite3.connect('exam.db')
    cursor = conn.cursor()

    # Створення таблиці links
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS links (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            link VARCHAR(50),
            name VARCHAR(20)
        )
    ''')

    # Створення таблиці result
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS result (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_choice INTEGER,
            result_value VARCHAR(50),
            FOREIGN KEY (user_choice) REFERENCES links (id)
        )
    ''')

    # Збереження змін у базі даних
    conn.commit()

    # Закриття з'єднання з базою даних
    conn.close()

def get_currency_rate():
    # Запит користувача на введення суми в гривнях
    amount_in_hrn = float(input("Введіть суму в гривнях: "))

    # Вибір з бази даних по id = 1 (валюта в NBU)
    bank_link = get_link_by_id(1)

    # Парсінг сайта NBU для отримання поточного курсу долара
    current_rate = parse_nbu_rate(bank_link)

    # Обчислення результату
    result = amount_in_hrn / current_rate

    # Виведення результату
    print(f"Курс: {current_rate}, Грн: {amount_in_hrn}, Результат: {result}")

    # Збереження результату в базу даних
    save_result(1, result)

def get_weather():
    # Вибір з бази даних по id = 2 (погода в Києві)
    weather_link = get_link_by_id(2)

    # Парсінг сайта для отримання інформації про погоду
    temperature = parse_weather(weather_link)

    # Виведення і збереження результату
    current_date = datetime.datetime.now().strftime("%d.%m")
    print(f"Дата: {current_date}, Температура: {temperature}")

    # Збереження результату в базу даних
    save_result(2, temperature)

def get_link_by_id(link_id):
    conn = sqlite3.connect('exam.db')
    cursor = conn.cursor()

    # Вибір з бази даних по id
    cursor.execute("SELECT link FROM links WHERE id = ?", (link_id,))
    link = cursor.fetchone()[0]

    conn.close()
    return link

def parse_nbu_rate(url):
    # Логіка парсінгу для отримання курсу долара
    # (замість цього додається просто фіктивне значення для прикладу)
    return 37.5

def parse_weather(url):
    # Логіка парсінгу для отримання температури
    # (замість цього додається просто фіктивне значення для прикладу)
    return "27+"

def save_result(user_choice, result_value):
    conn = sqlite3.connect('exam.db')
    cursor = conn.cursor()

    # Вставка результату в таблицю result
    cursor.execute("INSERT INTO result (user_choice, result_value) VALUES (?, ?)", (user_choice, result_value))

    # Збереження змін у базі даних
    conn.commit()

    conn.close()

# Вибір користувача
user_choice = int(input("Ваш вибір (1 або 2): "))

# Виклик функції для створення таблиць
create_tables()

# Виклик функції відповідно до вибору користувача
if user_choice == 1:
    get_currency_rate()
elif user_choice == 2:
    get_weather()
else:
    print("Некоректний вибір.")
