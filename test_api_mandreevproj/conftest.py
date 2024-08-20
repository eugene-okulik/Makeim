import pytest
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
