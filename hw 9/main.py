import requests
from bs4 import BeautifulSoup

class CurrencyConverter:
    def __init__(self):
        self.exchange_rates = self.get_exchange_rates()

    def get_exchange_rates(self):
        url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
        response = requests.get(url)
        data = response.json()
        exchange_rates = {item['cc']: item['rate'] for item in data}
        return exchange_rates

    def convert_to_usd(self, amount, currency_code):
        if currency_code.upper() in self.exchange_rates:
            rate = self.exchange_rates[currency_code.upper()]
            usd_amount = amount / rate
            return usd_amount
        else:
            return None

if __name__ == "__main__":
    converter = CurrencyConverter()

    amount_str = input("Введіть кількість вашої валюти: ")
    try:
        amount = float(amount_str)
    except ValueError:
        print("Будь ласка, введіть коректне число.")
        exit()

    currency_code = input("Введіть код вашої валюти (наприклад, USD, EUR, UAH): ")

    usd_amount = converter.convert_to_usd(amount, currency_code)
    if usd_amount is not None:
        print(f"{amount} {currency_code} = {usd_amount:.2f} USD")
    else:
        print("Валюта не знайдена. Будь ласка, введіть коректний код валюти.")
