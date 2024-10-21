import pandas as pd


def read_file_excel(file_path: str) -> list:
    """Функция считывает финансовые операции с файла с расширением форматов Excel"""
    file_excel = pd.read_excel(file_path)
    return file_excel.to_dict(orient="records")


def read_file_csv(file_path: str) -> list:
    """Функция считывает финансовые операции с файла с расширением .csv"""
    file_csv = pd.read_csv(file_path, sep=";")
    return file_csv.to_dict(orient="records")
