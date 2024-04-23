import requests


def post_a_post():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {"content-type": "application/json"}
    response = requests.post('https://api.restful-api.dev/objects', json=body, headers=headers).json()
    return response['id']


def put_a_post():
    post_id = post_a_post()
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


def patch_a_post():
    post_id = post_a_post()
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


def delete_a_post():
    post_id = post_a_post()
    response = requests.delete(f'https://api.restful-api.dev/objects/{post_id}')
    print(response)


post_a_post()
put_a_post()
patch_a_post()
delete_a_post()
