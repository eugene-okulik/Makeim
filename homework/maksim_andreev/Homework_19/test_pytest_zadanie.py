import allure
import requests
import pytest


@pytest.fixture(scope='session')
def start_end():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def before_after():
    print('before test')
    yield
    print('after test')


@pytest.fixture()
def post_and_delete():
    body = {"name": "Apple MacBook Pro 16", "data": {"year": 2019, "price": 1849.99,
            "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}}
    headers = {"content-type": "application/json"}
    response = requests.post('https://api.restful-api.dev/objects', json=body, headers=headers)
    assert response.status_code == 200
    assert response.json()['name'] == 'Apple MacBook Pro 16'
    post_id = response.json()['id']
    yield post_id
    requests.delete(f'https://api.restful-api.dev/objects/{post_id}')


@pytest.mark.critical
@allure.feature('API tests')
@allure.story('POST mtd')
@allure.title('Создание объекта')
@allure.epic('EPIC-7423')
@allure.description('Здесь мы пытаемся создать объект, в котором не должно быть ошибок. Раньше через раз тут была 500ка'
                    'на запросе')
def test_post_a_new_object(post_and_delete, start_end, before_after):
    with allure.step('Prepare test data'):
        body = {"name": "Apple MacBook Pro 16", "data": {"year": 2019, "price": 1849.99,
                "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}}
        headers = {"content-type": "application/json"}
    with allure.step('Run post request for new object'):
        response = requests.post('https://api.restful-api.dev/objects', json=body, headers=headers)
    with allure.step('Check response status (200)'):
        assert response.status_code == 200
    with allure.step('Check name for created object'):
        assert response.json()['name'] == 'Apple MacBook Pro 16'


@pytest.mark.critical
@allure.feature('API tests')
@allure.story('PUT mtd')
@allure.title('Полное обновление объекта методом PUT')
def test_put_a_post(post_and_delete, start_end, before_after):
    with allure.step('Prepare data for put to created object'):
        post_id = post_and_delete
        body = {
            "name": "Apple MacBook Pro 19",
            "data": {
                "year": 2019,
                "price": 2000.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }
        headers = {"content-type": "application/json"}
    with allure.step('Run put request for put data to created object'):
        response = requests.put(f'https://api.restful-api.dev/objects/{post_id}', json=body, headers=headers).json()
    with allure.step('Check name for created object'):
        assert response['name'] == 'Apple MacBook Pro 19'


@pytest.mark.medium
@allure.feature('API tests')
@allure.story('PATCH mtd')
@allure.title('Внесение изменения методом PATCH')
def test_patch_a_post(post_and_delete, before_after):
    with allure.step('Prepare data for patch object'):
        post_id = post_and_delete
        body = {
            "name": "Apple MacBook Pro 11",
            "data": {
                "price": 2000.99,
                "CPU model": "Intel Core i9"
            }
        }
        headers = {"content-type": "application/json"}
    with allure.step('Run request for patch created object'):
        response = requests.patch(f'https://api.restful-api.dev/objects/{post_id}', json=body, headers=headers).json()
    with allure.step('Check name as patch result'):
        assert response['name'] == 'Apple MacBook Pro 11'


@allure.feature('API tests')
@allure.story('DELETE mtd')
@allure.title('Удаление созданного объекта')
def test_delete_a_post(post_and_delete, before_after):
    post_id = post_and_delete
    with allure.step('Request to delete created object'):
        requests.delete(f'https://api.restful-api.dev/objects/{post_id}')
