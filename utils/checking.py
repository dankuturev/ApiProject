"""Методы для проверки ответов наших запросов"""
import json


class Checking:
    """Метод для проверки статус-кода"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code, 'Ошибка, код ответа не совпадает'
        print('Статус-код корректен')

    """Метод для проверки наличия полей в ответе запроса"""
    @staticmethod
    def check_json_token(result, expected_value: list):
        token = json.loads(result.text)
        assert list(token) == expected_value, 'Ошибка, отсуствуют обязательные поля'
        print("Все поля присутствуют")

    """Метод для проверки значения обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        print(check_info)
        assert check_info == expected_value
        print(field_name + " is correct")


