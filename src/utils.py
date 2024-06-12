import json
import os
from typing import Any, Dict, List

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def finance_data(path: str) -> List[Dict[str, float]]:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        with open(path, encoding="UTF-8") as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    return data
                else:
                    return []
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []


def get_exchange_rate(from_currency: str, to_currency: str = "RUB") -> Any:
    """Принимает код валюты, из которой нужно конвертировать и код валюты, в которую нужно конвертировать,
    возвращает текущий обменный курс."""
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={to_currency}&base={from_currency}"
    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)["rates"]["RUB"]
    return data


def get_sum_of_transaction(transaction: dict) -> float:
    """Принимает сумму и код валюты, возвращает сумму, конвертированную в рубли (RUB)."""
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return float(amount)
    elif currency in ["USD", "EUR"]:
        exchange_rate = get_exchange_rate(currency)
        result = float(amount) * exchange_rate
        return float(result)
    else:
        raise ValueError("Неподдерживаемая валюта!")
