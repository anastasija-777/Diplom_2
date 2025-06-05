import requests
import allure
from data import URL
from methods.create_user import CreateUser
from helper import modify_user


class LoginUser:

    @staticmethod
    def login_user(body):
        with allure.step('Создаем уникального пользователя.'):
            CreateUser.create_user(body)
        with allure.step('Из тела на запрос "Создание пользователя" получаем login и password для авторизации'):
            email = body['email']
            password = body['password']
            body_login = {
                "email": email,
                "password": password
            }
        with allure.step('Получает ответ на авторизацию пользователя'):
            response = requests.post(URL.LOGIN_USER_URL,data = body_login)
            return response

    @staticmethod
    def modify_login_user(body,key,value):
        with allure.step('Создаем уникального пользователя.'):
            CreateUser.create_user(body)
        with allure.step('Из тела на запрос "Создание пользователя" получаем login и password для авторизации'):
            email = body['email']
            password = body['password']
            body_login = {
                "email": email,
                "password": password
            }
        with allure.step('Меняем одно из обязательных полей для авторизации на неверное.'):
            modify_user(key, value, body_login)
        with allure.step('Получает ответ на авторизацию пользователя'):
            response = requests.post(URL.LOGIN_USER_URL, data=body_login)
            return response