from src.processing import decreasing_dates, key_value_output
from src.transaction_processing import find_operations_by_desc
from src.transactions_extentions import read_file_csv, read_file_excel
from src.utils import finance_data
from src.widget import mask_number


def main() -> None:
    """Функция отвечает за основную логику проекта, выполняя все написанные функции и связывая функциональности
    между собой"""
    user_input = int(
        input(
            "Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
            "Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из json файла\n"
            "2. Получить информацию о транзакциях из csv файла\n"
            "3. Получить информацию о транзакциях из xlsx файла\n"
        )
    )

    if user_input == 1:
        data = finance_data("data/operations.json")
        print("Для обработки выбран json файл.")
        print(data)
    elif user_input == 2:
        data = read_file_csv("data/transactions.csv")
        print("Для обработки выбран csv файл.")
    elif user_input == 3:
        data = read_file_excel("data/transactions_excel.xlsx")
        print("Для обработки выбран xlsx файл.")

    while True:
        status_input = input(
            "Введите статус по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        ).upper()

        if status_input in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f'Операции отфильтрованы по статусу "{status_input}"')
            list_transaction = key_value_output(data, status_input)
            print("Отсортировать операции по дате? Да/Нет\n")
            data_input = input().lower()
            if data_input == "да":
                print("Отсортировать по возрастанию или по убыванию?\n")
                increasing_input = input().lower()
                if increasing_input == "по возрастанию":
                    list_transaction = decreasing_dates(list_transaction, False)
                else:
                    list_transaction = decreasing_dates(list_transaction, True)
            print("Выводить только рублевые транзакции? Да/Нет\n")
            rub_input = input().lower()
            if rub_input == "да":
                currency_list = []

                for transaction in list_transaction:
                    if "currency_code" in transaction.keys():
                        if transaction["currency_code"] == "RUB":
                            currency_list.append(transaction)
                    elif transaction["operationAmount"]["currency"]["code"] == "RUB" and user_input not in [2, 3]:
                        currency_list.append(transaction)
            else:
                currency_list = list_transaction
            print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
            user_input_word = input().lower()
            if user_input_word == "да":
                currency_list = find_operations_by_desc(list_transaction, "Перевод организации")
            print("Распечатываю итоговый список транзакций...\n")
            if len(currency_list) > 0:
                print(f"Всего банковских операций в выборке: {len(currency_list)}")
                for currency in currency_list:
                    date = currency["date"]
                    description = currency["description"]
                    account_from = str(currency.get("from", "without_from"))
                    account_to = currency["to"]
                    if "amount" in currency:
                        amount = currency["amount"]
                    else:
                        amount = currency["operationAmount"]["amount"]

                    print(
                        f"{date} {description}",
                        f"\n{mask_number(account_from)} -> {mask_number(account_to)}",
                        f"\nСумма: {amount} руб.\n",
                    )
            else:
                print("Не найдено ни одной транзакции подходящей под ваши условия фильтрации")
                break
        else:
            print(f'Статус операции "{status_input}" недоступен.')


if __name__ == "__main__":
    main()
