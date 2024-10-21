def key_value_output(input_list: list, key_state: str = "EXECUTED") -> list:
    """Принимает на вход список словарей и возвращает список словарей, имеющих элемент state, равным key_state"""
#    new_list = []
#    for i in input_list:
#        if i["state"] == key_state:
#            new_list.append(i)
    return list(filter(lambda x: x.get("state", 0) == key_state, input_list))


def decreasing_dates(input_list: list, condition: bool = True) -> list:
    """Принимает на вход список словарей и возвращает его же, отсортированным по убыванию даты по ключу date"""
    return sorted(input_list, key=lambda x: x["date"], reverse=condition)
