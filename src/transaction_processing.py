import re
from collections import defaultdict
from typing import Any, DefaultDict, Dict, List


def find_operations_by_desc(operations: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """Функция возвращает список с операциями по описанию, указанному на входе функции"""
    result = []
    for operation in operations:
        if re.search(search_string, operation["description"], re.IGNORECASE):
            result.append(operation)
    return result


def categorize_operations(operations: List[Dict[str, Any]], categories: Dict[str, List[str]]) -> Dict[str, int]:
    """Функция категоризирует банковские операции по заданным категориям в виде словаря, в котором ключи - это названия
    категорий, а значения - количество операций в каждой категории"""
    category_count: DefaultDict[str, int] = defaultdict(int)
    for operation in operations:
        description = operation["description"]
        for category, keywords in categories.items():
            if any(keyword.lower() in description.lower() for keyword in keywords):
                category_count[category] += 1
                break

    return dict(category_count)
