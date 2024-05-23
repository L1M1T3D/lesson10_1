def mask_card_number(card_number: str) -> str:
    """Функция получает номер карты и возвращает замаскированный вид"""
    masked_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return masked_card_number


def mask_account_number(account_number: str) -> str:
    """Функция получает номер счёта и возвращает замаскированный вид"""
    masked_account_number = "**" + account_number[-4:]
    return masked_account_number
