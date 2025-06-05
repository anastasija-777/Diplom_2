import allure


@allure.step('Меняем значение ключа в теле эндпоинта "Создание пользователя".')
def modify_user(key,value,body):
    body_user = body
    body_user[key]=value
    return body_user

