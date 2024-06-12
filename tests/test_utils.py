import json
from typing import Any
from unittest.mock import Mock, mock_open, patch

from src.utils import finance_data, get_sum_of_transaction


@patch("requests.get")
def test_convert_to_rub_usd(mock_get: Any) -> None:
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "73.5", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }

    mock_response = Mock()
    mock_response.text = json.dumps({"rates": {"RUB": 100.0}})
    mock_get.return_value = mock_response

    amount_in_rub = get_sum_of_transaction(transaction)
    assert abs(amount_in_rub - 7350.0) < 1e-6


@patch("requests.get")
def test_convert_to_rub_eur(mock_get: Any) -> None:
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "88.5", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }

    mock_response = Mock()
    mock_response.text = json.dumps({"rates": {"RUB": 100.0}})
    mock_get.return_value = mock_response

    amount_in_rub = get_sum_of_transaction(transaction)
    assert abs(amount_in_rub - 8850.0) < 1e-6


def test_convert_to_rub_rub() -> None:
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "100.00", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    amount_in_rub = get_sum_of_transaction(transaction)
    assert abs(amount_in_rub - 100.0) < 1e-6


@patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
def test_read_transactions_from_json(mock_file: Mock) -> None:
    transactions = finance_data("dummy_path.json")
    assert transactions == [{"amount": 100, "currency": "USD"}]


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_read_transactions_from_json_empty(mock_file: Mock) -> None:
    assert finance_data("data/operations.json") == []


@patch("builtins.open", new_callable=mock_open, read_data='{"not": "list"}')
def test_read_transactions_from_json_invalid_format(mock_file: Mock) -> None:
    assert finance_data("data/operations.json") == []


@patch("builtins.open", new_callable=mock_open)
def test_read_transactions_from_json_file_not_found(mock_file: Mock) -> None:
    assert finance_data("data/operations1.json") == []
