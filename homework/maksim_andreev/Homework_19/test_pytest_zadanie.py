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
    post_id = response.json()['id']
    yield post_id
    requests.delete(f'https://api.restful-api.dev/objects/{post_id}')


@pytest.mark.critical
def test_put_a_post(post_and_delete, start_end, before_after):
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
    response = requests.put(f'https://api.restful-api.dev/objects/{post_id}', json=body, headers=headers).json()
    assert response['name'] == 'Apple MacBook Pro 19'


@pytest.mark.medium
def test_patch_a_post(post_and_delete, before_after):
    post_id = post_and_delete
    body = {
        "name": "Apple MacBook Pro 11",
        "data": {
            "price": 2000.99,
            "CPU model": "Intel Core i9"
        }
    }
    headers = {"content-type": "application/json"}
    response = requests.patch(f'https://api.restful-api.dev/objects/{post_id}', json=body, headers=headers).json()
    assert response['name'] == 'Apple MacBook Pro 11'


def test_delete_a_post(post_and_delete, before_after):
    post_id = post_and_delete
    requests.delete(f'https://api.restful-api.dev/objects/{post_id}')
