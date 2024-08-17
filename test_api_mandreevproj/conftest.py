import pytest
from endpoints.create_post import CreatePost
from endpoints.update_post import UpdatePost
from endpoints.modify_post import ModifyPost
from endpoints.delete_post import DeletePost


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def update_post_endpoint():
    return UpdatePost()


@pytest.fixture()
def modify_post_endpoint():
    return ModifyPost()


@pytest.fixture()
def delete_post_endpoint():
    return DeletePost()
