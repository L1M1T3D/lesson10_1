import json
import os
from typing import Any, Dict, List

import requests
from dotenv import load_dotenv

from src.logger import setup_logging

load_dotenv()
API_KEY = os.getenv("API_KEY")
logger = setup_logging("utils", "utils.log")


def finance_data(path: str) -> List[Dict[str, float]]:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    logger.info(f"start finance_data({path})...")
    try:
        with open(path, encoding="UTF-8") as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    logger.info(f"finance_data({path}) result = {data}")
                    return data
                else:
                    logger.info(f"finance_data({path}) result = []")
                    return []
            except json.JSONDecodeError:
                logger.error(f"finance_data({path}) result (with erorr) = []")
                return []
    except FileNotFoundError:
        logger.error(f"finance_data({path}) result (with erorr) = []")
        return []


def get_exchange_rate(from_currency: str, to_currency: str = "RUB") -> Any:
    """Принимает код валюты, из которой нужно конвертировать и код валюты, в которую нужно конвертировать,
    возвращает текущий обменный курс."""
    logger.info(f"start get_exchange_rate({from_currency}, {to_currency})...")
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={to_currency}&base={from_currency}"
    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)["rates"]["RUB"]
    logger.info(f"get_exchange_rate({from_currency}, {to_currency}) result = {data}")
    return data


def get_sum_of_transaction(transaction: dict) -> float:
    """Принимает сумму и код валюты, возвращает сумму, конвертированную в рубли (RUB)."""
    logger.info(f"start get_sum_of_transaction({transaction})...")
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        result = float(amount)
        logger.info(f"get_sum_of_transaction({transaction}) result = {result}")
        return result
    elif currency in ["USD", "EUR"]:
        exchange_rate = get_exchange_rate(currency)
        result = float(amount) * exchange_rate
        logger.info(f"get_sum_of_transaction({transaction}) result = {float(result)}")
        return float(result)
    else:
        logger.error(f'get_sum_of_transaction({transaction}) result = "Неподдерживаемая валюта!"')
        raise ValueError("Неподдерживаемая валюта!")
