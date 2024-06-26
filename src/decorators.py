from functools import wraps
from typing import Any, Callable, Union


def log(filename: Union[str, None] = None) -> Callable:
    """Декоратор для логирования выполнения функции."""

    def wrapper(func: Callable) -> Callable:
        """Обертка для функции, добавляющая логирование."""

        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            """Внутренняя функция, выполняющая логирование до и после вызова основной функции."""
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                log_to_file(message, filename)
                print(message)
                return result
            except Exception as e:
                message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
                print(message)
                log_to_file(message, filename)

        return inner

    return wrapper


def log_to_file(msg: str, filename: Union[str, None] = None) -> None:
    """Функция, принимающая сообщение и файл, куда нужно записать это сообщение о результате выполнения функции."""
    if filename:
        with open(filename, "a") as file:
            file.write(msg + "\n")
