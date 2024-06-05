from typing import Any

from src.decorators import log


def test_log_without_error_without_filename(capsys: Any) -> None:
    @log()
    def my_function(x: Any, y: Any) -> Any:
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_with_error_without_filename(capsys: Any) -> None:
    @log()
    def my_function(x: Any, y: Any) -> Any:
        return x + y

    my_function("1", 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: can only concatenate str (not \"int\") to str. Inputs: ('1', 2), {}\n"


def test_log_with_error_with_filename(capsys: Any) -> None:
    @log(filename="mylog.txt")
    def my_function(x: Any, y: Any) -> Any:
        return x + y

    my_function("1", 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: can only concatenate str (not \"int\") to str. Inputs: ('1', 2), {}\n"


def test_log_without_error_with_filename(capsys: Any) -> None:
    @log(filename="mylog.txt")
    def my_function(x: Any, y: Any) -> Any:
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"
