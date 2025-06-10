import pytest
import requests
import allure
from generators import generate_body_create_user
from data import URL
from methods.create_order import CreateOrder
from methods.get_order_user import GetOrderUser


@allure.step('Генерируем тело эндпоинта "Создание пользователя" и при успешной авторизации после теста удаляем данного пользователя.')
@pytest.fixture(scope = "function")
def body_create_user():
    body = generate_body_create_user()

    yield body
    email = body['email']
    password = body['password']
    login_user = {
        "email": email,
        "password": password
    }
    response = requests.post(URL.LOGIN_USER_URL,data = login_user)
    if response.status_code == 200:
        json_response = response.json()
        token = json_response['accessToken']
        headers = {'Authorization': token}
        requests.delete(URL.DELETE_USER_URL,data = login_user,headers = headers)

@allure.step('Создаем пользователя, из ответа получаем токен и при успешной изменении данных пользователя после теста удаляем данного пользователя.')
@pytest.fixture(scope = "function")
def headers():
    body = generate_body_create_user()
    response = requests.post(URL.CREATE_USER_URL, data=body)
    if response.status_code == 200:
        json_response = response.json()
        token = json_response['accessToken']
        headers = {'Authorization': token}

        yield headers
        requests.delete(URL.DELETE_USER_URL,headers = headers)

@allure.step('Создаем экземпляр класса CreateOrder.')
@pytest.fixture(scope = "function")
def create_order():
    return CreateOrder

@allure.step('Создаем экземпляр класса GetOrderUser.')
@pytest.fixture(scope = "function")
def get_order_user():
    return GetOrderUser







