import requests
import allure
from data import URL


class CreateOrder:

    @staticmethod
    def create_order(headers,list_ingredients):
        with allure.step('Определяем переменную body для запроса "Создание заказа".'):
            body = {
                 "ingredients": list_ingredients
              }
        with allure.step('Получаем ответ на запрос "Создание заказа".'):
            response = requests.post(URL.CREATE_ORDER_URL,data = body, headers = headers)
        return response




