import pytest
import allure
from methods.create_order import CreateOrder
from data import Data

class TestCreateOrder:

    @allure.title('Тестируем успешное создание заказа.')
    def test_create_order_success(self,headers):
        with allure.step('Получаем токен для запроса "Создание заказа".'):
            headers=headers
        with allure.step('Получаем ответ на запрос "Создание заказа".'):
            response = CreateOrder.create_order(headers,Data.list_ingredients_correct)
        with allure.step('Проверяем код ответа на запрос "Создание пользователя".'):
            assert response.status_code == 200
        with allure.step('Проверяем, что ответа на запрос "Создание пользователя" содержит "order".'):
             assert 'order' in response.text

    @allure.title('Тестируем, что нельзя создать заказ без авторизации.')
    def test_create_order_without_login(self,create_order):
        with allure.step('Получаем ответ на запрос "Создание заказа" без авторизации.'):
            response = CreateOrder.create_order(None,Data.list_ingredients_correct)
            response_json = response.json()
        with allure.step('Проверяем код ответа на запрос "Создание пользователя" без авторизации.'):
            assert response.status_code == 401
        with allure.step('Проверяем, что ответ на запрос "Создание пользователя" без авторизации содержит "success":False и "message":"You should be authorised".'):
            assert response_json['success'] == False
            assert response_json['message'] == 'You should be authorised'

    @allure.title('Тестируем, что нельзя создать заказ без ингредиентов.')
    def test_create_order_without_ingredients(self,headers):
        with allure.step('Получаем токен для запроса "Создание заказа".'):
            headers=headers
        with allure.step('Получаем ответ на запрос "Создание заказа" без ингредиентов.'):
            response = CreateOrder.create_order(headers,'')
            response_json = response.json()
        with allure.step('Проверяем код ответа на запрос "Создание пользователя" без ингредиентов.'):
            assert response.status_code == 400
        with allure.step('Проверяем, что ответ на запрос "Создание пользователя" без ингредиентов содержит "success":False и "message":"Ingredient ids must be provided".'):
            assert response_json['success'] == False
            assert response_json['message'] == 'Ingredient ids must be provided'

    @allure.title('Тестируем, что нельзя создать заказ с неверным хешем ингредиентов.')
    def test_create_order_incorrect_hash(self,headers):
        with allure.step('Получаем токен для запроса "Создание заказа".'):
            headers=headers
        with allure.step('Получаем ответ на запрос "Создание заказа" с неверным хешем ингредиентов.'):
            response = CreateOrder.create_order(headers,Data.list_ingredients_incorrect)
        with allure.step('Проверяем код ответа на запрос "Создание пользователя" с неверным хешем ингредиентов.'):
            assert response.status_code == 500

