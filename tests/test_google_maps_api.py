from utils.api import GoogleMapsApi
from utils.checking import Checking
import allure
"""Создание, изменение и удаление новой локации"""

@allure.epic("Создает новую локацию")
class TestCreatePlace:
    @allure.description("Создание, изменение и удаление локации")
    def test_create_new_place(self):
        print("Метод POST")
        result_post = GoogleMapsApi.create_new_place()  # вызов метода по созданию новой локации
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        # token = json.loads(result_post.text)
        # print(list(token))
        Checking.check_json_value(result_post, 'status', 'OK')

        print('Метод GET')
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,
                                  ['location', 'accuracy', 'name', 'phone_number',
                                   'address', 'types', 'website', 'language'])
        # token = json.loads(result_get.text)
        # print(list(token))
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print('Метод PUT')
        result_put = GoogleMapsApi.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("Метод GET PUT")
        result_get = GoogleMapsApi.get_new_place(place_id)  # отправка метода Get
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,
                                  ['location', 'accuracy', 'name', 'phone_number',
                                   'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print("Метод DELETE")
        result_delete = GoogleMapsApi.delete_new_place(place_id)  # отправка метода Get
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')

        print("Метод GET DELETE")
        result_get = GoogleMapsApi.get_new_place(place_id)  # отправка метода Get
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])
