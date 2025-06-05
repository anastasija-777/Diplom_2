import allure
from methods.get_order_user import GetOrderUser


class TestGetOrderUser:

    @allure.title('Тестируем получение заказов конкретного пользователя с авторизацией.')
    def test_get_order_user_with_login(self,headers):
        with allure.step('Получаем токен для запроса "Получение заказов конкретного пользователя".'):
            headers=headers
        with allure.step('Получаем ответ на запрос "Получение заказов конкретного пользователя" с авторизацией.'):
            response = GetOrderUser.get_order_user(headers)
        with allure.step('Проверяем код ответа на запрос "Получение заказов конкретного пользователя" с авторизацией.'):
            assert response.status_code == 200
        with allure.step('Проверяем, что ответ на запрос "Получение заказов конкретного пользователя" с авторизацией содержит "orders" и "total".'):
            assert "orders" in response.text
            assert "total" in response.text

    @allure.title('Тестируем получение заказов конкретного пользователя без авторизации.')
    def test_get_order_user_without_login(self,get_order_user):
        with allure.step('Получаем ответ на запрос "Получение заказов конкретного пользователя" без авторизации.'):
            response = GetOrderUser.get_order_user(None)
            response_json = response.json()
        with allure.step('Проверяем код ответа на запрос "Получение заказов конкретного пользователя" без авторизации.'):
            assert response.status_code == 401
        with allure.step('Проверяем, что ответ на запрос "Получение заказов конкретного пользователя" без авторизации содержит "success":False и "message":"You should be authorised".'):
            assert response_json['success'] == False
            assert response_json['message'] == 'You should be authorised'