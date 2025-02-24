import allure
import requests

from utils.logger import Logger

"""Список HTTP методов"""


class HttpMethods:
    headers = {
        'Content-Type': 'application/json'
    }
    cookie = ''

    @staticmethod  # @staticmethod — это декоратор в Python, который используется для определения статического метода
    # в классе. Статические методы не требуют создания экземпляра класса для их вызова и не имеют доступа к атрибутам
    # или методам экземпляра (то есть они не принимают self в качестве первого аргумента). Вместо этого они могут
    # быть вызваны непосредственно через класс.
    def get(url):
        with allure.step("GET"):
            Logger.add_request(url, method="GET")
            result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def post(url, body):
        with allure.step("POST"):
            Logger.add_request(url, method="POST")
            result = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def put(url, body):
        with allure.step("PUT"):
            Logger.add_request(url, method="PUT")
            result = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step("DELETE"):
            Logger.add_request(url, method="DELETE")
            result = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            return result