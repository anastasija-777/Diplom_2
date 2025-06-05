import allure
from faker import Faker


@allure.step('Генерируем тело для создания уникального пользователя.')
def generate_body_create_user():
    faker = Faker()
    email = faker.email()
    password = faker.random_int(min=1000,max=999999)
    name = faker.name()
    body = {
        "email": email,
        "password": password,
        "name": name
    }
    return body