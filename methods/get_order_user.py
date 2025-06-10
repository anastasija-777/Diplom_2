import requests
import allure
from data import URL


class GetOrderUser:

    @staticmethod
    def get_order_user(headers):
        with allure.step('Получаем ответ на запрос "Получение заказов конкретного пользователя".'):
            response = requests.get(URL.GET_ORDER_USER_URL,headers=headers)
            return response

