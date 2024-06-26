import pytest

from src.masks import mask_account_number, mask_card_number


@pytest.fixture
def private_card_number() -> str:
    return "7000792289606361"


@pytest.fixture
def private_account_number() -> str:
    return "64686473678894779589"


def test_mask_card_number(private_card_number: str) -> None:
    assert mask_card_number(private_card_number) == "7000 79** **** 6361"


def test_mask_account_number(private_account_number: str) -> None:
    assert mask_account_number(private_account_number) == "**9589"
