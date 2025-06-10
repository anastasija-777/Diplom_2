import pytest
import allure
from methods.create_user import CreateUser
from helper import modify_user


class TestCreateUser:

    @allure.title('Тестируем успешную регистрацию уникального пользователя.')
    def test_create_user_unique_success(self,body_create_user):
        with allure.step('Генерируем тело для создания уникального пользователя.'):
            body = body_create_user
        with allure.step('Получаем ответ на запрос "Создание пользователя".'):
            response = CreateUser.create_user(body)
            response_json = response.json()
        with allure.step('Проверяем код ответа на запрос "Создание пользователя".'):
            assert response.status_code == 200
        with allure.step('Проверяем, что ответ на запрос "Создание пользователя" содержит "success": True .'):
            assert response_json['success'] == True

    @allure.title('Тестируем, что нельзя создать пользователя, который уже зарегистрирован.')
    def test_create_user_not_unique_error(self,body_create_user):
        with allure.step('Генерируем тело для создания уникального пользователя.'):
            body = body_create_user
        with allure.step('Создаем уникального пользователя.'):
            CreateUser.create_user(body)
        with allure.step('Получаем ответ на попытку создать пользователя, который уже зарегистрирован.'):
            response = CreateUser.create_user(body)
            response_json = response.json()
        with allure.step('Проверяем код ответа на попытку создать пользователя, который уже зарегистрирован.'):
            assert response.status_code == 403
        with allure.step('Проверяем, что ответ на попытку создать пользователя, который уже зарегистрирован содержит ""success": False" и ""message":"User already exists"".'):
            assert response_json['success'] == False
            assert response_json['message'] == 'User already exists'

    @allure.title('Тестируем, что нельзя создать пользователя если не заполнить одно из обязательных полей.')
    @pytest.mark.parametrize('key,value',[['email',''],['password',''],['name','']])
    def test_create_user_not_filled_email_error(self,body_create_user,key,value):
        with allure.step('Генерируем тело для создания уникального пользователя.'):
            body = body_create_user
        with allure.step('Меняем одно из обязательных полей для создания уникального пользователя на пустое.'):
            modify_user(key,value,body)
        with allure.step('Получаем ответ на попытку создать пользователя, если не заполнить одно из обязательных полей.'):
            response = CreateUser.create_user(body)
            response_json = response.json()
        with allure.step('Проверяем код ответа на попытку создать пользователя, если не заполнить одно из обязательных полей.'):
            assert response.status_code == 403
        with allure.step('Проверяем, что ответ на попытку создать пользователя, если не заполнить одно из обязательных полей содержит ""success": False" и ""message":"Email, password and name are required fields"".'):
            assert response_json['success'] == False
            assert response_json['message'] == 'Email, password and name are required fields'
