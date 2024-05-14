from src.masks import mask_account_number, mask_card_number


def mask_number(number: str) -> str:
    """Функция принимает строку с номером счёта/карты и возвращает маскированный вид"""
    new_number = number.split(" ")
    fixed_list = []
    for i in new_number:
        if not i.isdigit():
            fixed_list.append(i)
    for i in fixed_list:
        new_number.remove(i)
    fixed_number = "".join(new_number)
    fixed_str = " ".join(fixed_list)
    if len(fixed_number) > 16:
        masked_number = fixed_str + " " + mask_account_number(fixed_number)
    else:
        masked_number = fixed_str + " " + mask_card_number(fixed_number)
    return masked_number


def refactor_the_date(date: str) -> str:
    """Функция, принимающая дату в непривычном формате и возвращает в привычном"""
    new_date = date.split("T")
    return ".".join(list(reversed(new_date[0].split("-"))))
