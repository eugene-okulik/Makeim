import pytest
import requests
from endpoints.create_object import CreateObject
from endpoints.update_object import UpdateObject
from endpoints.modify_object import ModifyObject
from endpoints.delete_object import DeleteObject


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def modify_object_endpoint():
    return ModifyObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def create_new_object_endpoint(headers=None):
    payload = {"name": "Apple MacBook Pro 16", "data": {"year": 2019, "price": 1849.99,
                                                        "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}}
    response = requests.post(
        url='https://api.restful-api.dev/objects',
        json=payload,
        headers=headers
    )
    return response
