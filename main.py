import requests
from datetime import datetime
# Получаем текущую дату
today = datetime.now()
# Форматируем дату в удобный вид
formatted_date = today.strftime("%d-%m-%Y")  # Формат: ДД-ММ-ГГГГ

def get_exchange_rate(currency):
    url = "https://www.cbr-xml-daily.ru/latest.js"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rates = data.get('rates', {})
        date = data.get('Date')
        # Получаем дату из ответа API, используя get для предотвращения KeyError
        if date == None:
            date =today
            return rates.get(currency.upper()), date
        else:
            return rates.get(currency.upper()), date
            print(date)
    else:
        print("Ошибка при получении данных с API Центробанка.")
        return None, None

def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

def main():
    print("Конвертация валют")
    amount = float(input("Введите сумму в рублях: "))
    currency = input("Введите валюту для конвертации (EUR или USD): ").upper()

    exchange_rate, date = get_exchange_rate(currency)

    if exchange_rate is not None:  # Проверяем, что exchange_rate не None
        converted_amount = convert_currency(amount, exchange_rate)
        print(f"\nКурс {currency} к рублю на {date}: {exchange_rate}")
        print(f"Сумма в {currency}: {converted_amount:.2f} {currency}")
        print(f"Сумма в рублях: {amount:.2f} RUB")
    else:
        print("Не удалось получить курс валют.")

if __name__ == "__main__":  # Исправлено условие для запуска главной функции
    main()