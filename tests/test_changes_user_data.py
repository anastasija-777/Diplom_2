import pytest
import allure
import requests
from data import URL
from data import Data


class TestChangesUserData:

    @allure.title('Тестируем успешное изменение пользовательских данных с авторизацией.')
    @pytest.mark.parametrize('key,value',[['email',Data.email],['name',Data.name]])
    def test_changes_user_data_login(self, headers,key,value):
        with allure.step('Получаем токен для запроса "Изменения данных пользователя".'):
            headers = headers
        with allure.step('Получаем ответ на запрос "Изменение данных пользователя".'):
            response = requests.patch(URL.CHANGES_USER_DATA_URL, headers=headers, json={key:value})
            response_json = response.json()
        with allure.step('Проверяем код ответа на запрос "Изменение данных пользователя".'):
            assert response.status_code == 200
        with allure.step('Проверяем что данные действительно изменились.'):
            assert response_json['user'][key] == value

    @allure.title('Тестируем,что нельзя изменить пользовательские данные без авторизации.')
    @pytest.mark.parametrize('key,value', [['email', Data.email], ['name', Data.name]])
    def test_changes_user_data_without_login(self, key, value):
        with allure.step('Получаем ответ на запрос "Изменение данных пользователя" без авторизации.'):
            response = requests.patch(URL.CHANGES_USER_DATA_URL, json={key: value})
            response_json = response.json()
        with allure.step('Проверяем код ответа на запрос "Изменение данных пользователя" без авторизации.'):
            assert response.status_code == 401
        with allure.step('Проверяем, что ответ на попытку изменить данные пользователя без авторизации "success": False и "message":"You should be authorised".'):
            assert response_json['success'] == False
            assert response_json['message'] == 'You should be authorised'









