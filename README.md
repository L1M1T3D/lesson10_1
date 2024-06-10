# Дошашка по уроку 12.1 на Skypro
Содержит новый модуль `utils.py` и в ней **декоратор**, способный засчитывать ошибки функции и вписывать их в файл
и **тестирования** для этих же функций

## Использование
Использовать тесты можно для проверки работоспособности декоратора. **Также**, можно проверять файл, который создаётся
и пополняется при тестировании

### Тестирование
Используя **Pytest** (_фреймворк для тестирования кода/функций проекта_), можно его активировать, введя команду в
терминале - `pytest --cov tests/`. Тем самым проверится вся директория `tests/` и в терминале выведется вся информация
о них. Также можно заглянуть в директорию `htmlcov/` и обнаружить там файл `index.html`, в котором уже
продемонстрированы весь **code coverage** тестов. Запустить данное действие заново - 
`pytest --cov=src --cov-report=html`.

## Разработчик проекта
**Илья Топко** — миллиардер, плейбой, филантроп