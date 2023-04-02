def filter_query(value, data):
    """
    Функция фильтрации данных.
    :param value:
    :param data:
    :return: отфильтрованный список по параметру value.
    """
    return filter(lambda x: value in x, data)


def map_query(value, data):
    """
    Функция изменения вида исходных данных.
    :param value:
    :param data:
    :return: возвращает колонку из данных по параметру value.
    """
    idx = int(value)
    return map(lambda x: x.split(' ')[idx], data)


def unique_query(data):
    """
    Функция для выявления уникальных значений.
    :param data:
    :return: список уникальных значений на основе данных(data).
    """
    return set(data)


def sorted_query(value, data):
    """
    Функция сортировки данных.
    :param value:
    :param data:
    :return: список отсортированных данных по параметру value(asc/desc).
    """
    reverse = value == 'desc'
    return sorted(data, reverse=reverse)


def limit_query(data, value):
    """
    Функция лимитирования данных.
    :param data:
    :param value:
    :return: Список длинной по параметру value.
    """
    limit = int(value)
    return list(data)[:limit]
