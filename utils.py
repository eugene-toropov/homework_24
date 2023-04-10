import re
from typing import Iterable, List, Set, Iterator


def filter_query(value: str, data: Iterable[str]) -> Iterator[str]:
    """
    Функция фильтрации данных.
    :param value:
    :param data:
    :return: отфильтрованный список по параметру value.
    """
    return filter(lambda x: value in x, data)


def map_query(value: str, data: Iterable[str]) -> Iterator[str]:
    """
    Функция изменения вида исходных данных.
    :param value:
    :param data:
    :return: возвращает колонку из данных по параметру value.
    """
    idx = int(value)
    return map(lambda x: x.split(' ')[idx], data)


def unique_query(data: Iterable[str]) -> Set[str]:
    """
    Функция для выявления уникальных значений.
    :param data:
    :return: список уникальных значений на основе данных(data).
    """
    return set(data)


def sorted_query(value: str, data: Iterable[str]) -> List[str]:
    """
    Функция сортировки данных.
    :param value:
    :param data:
    :return: список отсортированных данных по параметру value(asc/desc).
    """
    reverse: bool = value == 'desc'
    return sorted(data, reverse=reverse)


def limit_query(value: str, data: Iterable[str]) -> List[str]:
    """
    Функция лимитирования данных.
    :param data:
    :param value:
    :return: Список длинной по параметру value.
    """
    limit = int(value)
    return list(data)[:limit]


def regex_query(value: str, data: Iterable[str]) -> Iterator[str]:
    """
    Функция поиска подстрок в строке при помощи регулярных выражений
    :param value:
    :param data:
    :return отфильтрованный список по параметру value:
    """
    res = re.compile(value)
    return filter(lambda x: re.search(res, x), data)
