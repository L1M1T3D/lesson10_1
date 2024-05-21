import pytest
from src.widget import refactor_the_date, mask_number

@pytest.fixture
def date():
    return "2020-10-11T02:26:18.671407"


def test_refactor_the_date(date):
    assert refactor_the_date(date) == "11.10.2020"


@pytest.mark.parametrize("number, expected_result", [("Visa Platinum 7000 7922 8960 6361", "Visa Platinum 7000 79** **** 6361"),
                                                     ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                                     ("Счет 73654108430135874305", "Счет **4305")])
def test_mask_number(number, expected_result):
    assert mask_number(number) == expected_result
