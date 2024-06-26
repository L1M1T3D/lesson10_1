from typing import Dict, Generator, List


def filter_by_currency(transactions: List[Dict[str, dict]], currency: str) -> Generator:
    """Функция принимает список словарей с банковскими операциями и возвращает итератор,
    который выдает по очереди  операции, в которых указана заданная валюта (currency)"""
    while True:
        for i, z in enumerate(transactions):
            if transactions[i]["operationAmount"]["currency"]["code"] == currency:
                yield transactions[i]["id"]


def transaction_descriptions(transactions: List[Dict[str, dict]]) -> Generator:
    """Функция принимает список словарей с банковскими операциями и возвращает описание каждой операции по очереди."""
    for i, z in enumerate(transactions):
        yield transactions[i]["description"]


def card_number_generator(start: int, end: int) -> Generator:
    """Функция принимает диапазон, в котором будут генерироваться номера банковских карт, используя формат XXXX XXXX
    XXXX XXXX."""
    for i in range(start, end + 1):
        num = f"{i:016}"
        card_number = f"{num[:4]} {num[4:8]} {num[8:12]} {num[12:16]}"
        yield card_number
