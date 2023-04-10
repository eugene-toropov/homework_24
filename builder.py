from utils import filter_query, sorted_query, map_query, limit_query, unique_query, regex_query
from typing import Iterable, Optional, List, Iterator, Dict, Callable

CMD_TO_FUNCTIONS: Dict[str, Callable] = {
    'filter': filter_query,
    'sort': sorted_query,
    'map': map_query,
    'limit': limit_query,
    'unique': unique_query,
    'regex': regex_query,
}  # Словарь с объектами функций с соответствующими именами из запроса


def read_file(file_name: str) -> Iterator[str]:
    """
    Функция чтения файла.
    :param file_name:
    :return: генератор данных на основе файла.
    """
    with open(file_name) as file:
        for line in file:
            yield line


def build_query(cmd: str, value: str, file_name: str, data: Optional[Iterable[str]]) -> List[str]:
    """
    Функция построения запроса.
    :param cmd:
    :param value:
    :param file_name:
    :param data:
    :return: результат вызванной функции(cmd) в виде списка.
    """
    if data is None:
        res: Iterable[str] = read_file(file_name)
    else:
        res = data

    return list(CMD_TO_FUNCTIONS[cmd](value=value, data=res))
