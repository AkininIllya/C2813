import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime


def get_weather_data():
    url = "https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D0%B5%D0%B2"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Знайдемо елемент з температурою
    temperature_element = soup.find('div', {'class': 'today_nowcard-temp'})

    # Отримаємо температуру (припускаємо, що температура знаходиться у цьому елементі)
    temperature = float()

    return temperature


def save_to_database(date_time, temperature):
    # Підключення до БД
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()

    # Вставка даних в таблицю
    cursor.execute('INSERT INTO weather (date_time, temperature) VALUES (?, ?)', (date_time, temperature))

    # Збереження змін у БД
    conn.commit()

    # Закриття з'єднання
    conn.close()


if __name__ == "__main__":
    # Отримання поточної дати та часу
    current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Отримання температури
    temperature = get_weather_data()

    # Збереження в БД
    save_to_database(current_date_time, temperature)

    print(f"Дані успішно збережено в БД: {current_date_time}, Температура: {temperature}°C")