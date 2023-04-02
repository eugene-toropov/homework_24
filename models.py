from marshmallow import Schema, fields, validate

VALID_CMD_COMMANDS = ('filter', 'unique', 'map', 'limit', 'sort')  # Список команд из запроса для проверки


class RequestSchema(Schema):
    """
    Схема сериализации/десериализации запроса.
    """
    cmd1 = fields.Str(required=True, validate=validate.OneOf(VALID_CMD_COMMANDS))
    value1 = fields.Str(required=True)
    cmd2 = fields.Str(required=True, validate=validate.OneOf(VALID_CMD_COMMANDS))
    value2 = fields.Str(required=True)
    file_name = fields.Str(required=True)