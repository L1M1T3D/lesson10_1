from src.logger import setup_logging

logger = setup_logging("masks", "masks.log")


def mask_card_number(card_number: str) -> str:
    """Функция получает номер карты и возвращает замаскированный вид"""
    logger.info(f"start card_number({card_number})...")
    masked_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    logger.info(f"card_number({card_number}) result = {masked_card_number}")
    return masked_card_number


def mask_account_number(account_number: str) -> str:
    """Функция получает номер счёта и возвращает замаскированный вид"""
    logger.info(f"start card_number({account_number})...")
    masked_account_number = "**" + account_number[-4:]
    logger.info(f"mask_account_number({account_number}) result = {masked_account_number}")
    return masked_account_number
