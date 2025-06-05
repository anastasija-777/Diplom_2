import requests
import allure
from data import URL


class ChangesUserData:

    @staticmethod
    def changes_user_data(headers,key,value):
        with allure.step('Получаем ответ на запрос "Изменение данных пользователя".'):
            response = requests.patch(URL.CHANGES_USER_DATA_URL, headers = headers,json = {key:value})
            return response

