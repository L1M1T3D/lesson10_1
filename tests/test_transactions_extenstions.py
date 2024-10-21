import csv
import os
from unittest.mock import Mock, mock_open, patch

from pandas import DataFrame

from src.transactions_extentions import read_file_excel

csv_data = (
    "id;state;date;amount;currency_name;currency_code;from;to;description\n"
    "650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод "
    "организации"
)

mock_csv_file = mock_open(read_data=csv_data)


@patch("builtins.open", mock_csv_file)
def test_read_csv() -> None:
    rows = []
    with open("../data/transactions.csv") as csv_file:
        for row in csv.reader(csv_file):
            rows.append(row)

    assert rows != [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
        }
    ]


@patch("pandas.read_excel")
def test_read_excel(mock_open_excel: Mock) -> None:

    mock_open_excel.return_value = DataFrame(
        {
            "id": [650703.0],
            "state": ["EXECUTED"],
            "date": ["2023-09-05T11:30:32Z"],
            "amount": [16210.0],
            "currency_name": ["Sol"],
            "currency_code": ["PEN"],
            "from": ["Счет 58803664561298323391"],
            "to": ["Счет 39745660563456619397"],
            "description": ["Перевод организации"],
        }
    )
    assert read_file_excel(os.path.join("data/transactions_excel.xlsx")) == [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
