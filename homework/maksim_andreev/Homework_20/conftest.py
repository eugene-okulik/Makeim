import pytest
import requests


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
    