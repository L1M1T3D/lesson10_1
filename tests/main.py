from src.widget import mask_number, refactor_the_date

card_num1 = "Visa Platinum 7000 7922 8960 6361"
card_num2 = "Maestro 1596837868705199"
acc_num1 = "Счет 64686473678894779589"
acc_num2 = "Счет 73654108430135874305"
date1 = "2020-10-11T02:26:18.671407"
date2 = "2023-12-19T13:21:86.675477"


print(mask_number(card_num1))
print(mask_number('Visa Platinum 7000 7922 8960 6361'))
print(mask_number(card_num2))
print(mask_number(acc_num1))
print(mask_number(acc_num2))
print(refactor_the_date(date1))
print(refactor_the_date(date2))
