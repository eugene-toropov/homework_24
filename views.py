from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from builder import build_query
from models import RequestSchema

main_bp = Blueprint('main', __name__)  # Создаем неймспейс


@main_bp.route('/perform_query', methods=['POST'])
def perform_query():
    """
    Представление по маршруту '/perform_query', метод = POST.
    Данные из запроса прогоняем через схему RequestSchema().
    Получаем результат запроса по первым двум параметрам при помощи функции build_query() -> first_result
    Данные из first_result прогоняем через вторую пару параметров -> result
    Возвращаем их пользователю в формате json.
    """
    data = request.json

    try:
        RequestSchema().load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400

    first_result = build_query(
        cmd=data['cmd1'],
        value=data['value1'],
        data=None,
        file_name=data['file_name'],
    )

    result = build_query(
        cmd=data['cmd2'],
        value=data['value2'],
        data=first_result,
        file_name=data['file_name'],
    )

    return jsonify(result)
