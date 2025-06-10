import allure
import pytest
from methods.login_user import LoginUser
from data import Data


class TestLoginUser:

     @allure.title('Тестируем успешную авторизацию пользователя.')
     def test_login_user_success(self,body_create_user):
         with allure.step('Генерируем тело для создания уникального пользователя.'):
             body = body_create_user
         with allure.step('Получает ответ на авторизацию пользователя'):
             response_login = LoginUser.login_user(body)
             response_login_json = response_login.json()
         with allure.step('Проверяем код ответа на запрос о авторизации пользователя'):
             assert response_login.status_code == 200
         with allure.step('Проверяем, что ответ на запрос о авторизации пользователя содержит ""success": True".'):
             assert response_login_json['success'] == True

     @pytest.mark.parametrize('key,value',[['email',Data.email],['password',Data.password]])
     @allure.title('Тестируем ошибку при авторизации с неверным логином и паролем')
     def test_login_user_not_true_email_password_error(self, body_create_user,key,value):
         with allure.step('Генерируем тело для создания уникального пользователя.'):
             body = body_create_user
         with allure.step('Получает ответ на авторизацию пользователя при неверном логине/пароле'):
             response_login = LoginUser.modify_login_user(body,key,value)
             response_login_json = response_login.json()
         with allure.step('Проверяем код ответа на запрос о авторизации пользователя при неверном логине/пароле'):
             assert response_login.status_code == 401
         with allure.step('Проверяем, что ответ содержит "success": False и "message": "email or password are incorrect".'):
             assert response_login_json['success'] == False
             assert response_login_json['message'] == 'email or password are incorrect'





