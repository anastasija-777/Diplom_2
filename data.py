class URL:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'
    CREATE_USER_URL = BASE_URL + '/api/auth/register'
    DELETE_USER_URL = BASE_URL + '/api/auth/user'
    LOGIN_USER_URL = BASE_URL + '/api/auth/login'
    CHANGES_USER_DATA_URL = BASE_URL + '/api/auth/user'
    CREATE_ORDER_URL = BASE_URL + '/api/orders'
    GET_ORDER_USER_URL = BASE_URL + '/api/orders'

class Data:
    email = 'hogwarts@yandex.ru'
    password = 123456
    name = 'hogwarts'
    list_ingredients_correct = ['61c0c5a71d1f82001bdaaa6d','61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa77']
    list_ingredients_incorrect = ['61c0c5a71d1ff82001bdaaa6d','61c0c5a71d1f82001bdaaa73']
