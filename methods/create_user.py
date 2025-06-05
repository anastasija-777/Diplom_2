import requests
import allure
from data import URL


class CreateUser:

    @staticmethod
    def create_user(body):
        with allure.step('Получаем ответ на запрос "Создание пользователя".'):
            response = requests.post(URL.CREATE_USER_URL,data=body)
            return response