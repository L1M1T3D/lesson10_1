import json
import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

transaction = {
  "id": 441945886,
  "state": "EXECUTED",
  "date": "2019-08-26T10:50:58.294041",
  "operationAmount": {
    "amount": "319.58",
    "currency": {
      "name": "руб.",
      "code": "USD"
    }
  },
  "description": "Перевод организации",
  "from": "Maestro 1596837868705199",
  "to": "Счет 64686473678894779589"
}


def finance_data(path: str) -> list:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        with open(path, encoding='UTF-8') as f:
            try:
                data = json.load(f)
                return data
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []


def get_exchange_rate(from_currency: str, to_currency='RUB') -> Any:
    """Принимает на вход валюту"""
    url = f'https://api.apilayer.com/exchangerates_data/latest?symbols={to_currency}&base={from_currency}'
    headers = {
        'apikey': API_KEY
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    if to_currency in data['rates']:
        return data['rates'][to_currency]


def get_sum_of_transaction(transaction: dict) -> float:
    amount = transaction['operationAmount']['amount']
    currency = transaction['operationAmount']['currency']['code']
    if currency == 'RUB':
        return float(amount)
    elif currency in ['USD', 'EUR']:
        exchange_rate = get_exchange_rate(currency)
        result = float(amount) * exchange_rate
        return float(result)
