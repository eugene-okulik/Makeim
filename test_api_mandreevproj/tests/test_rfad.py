import pytest

TEST_DATA = [
    {"name": "Apple MacBook Pro 16", "data": {"year": 2019, "price": 1849.99,
                                              "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}},
    {"name": "Apple MacBook Pro 19", "data": {"year": 2021, "price": 1849.99,
                                              "CPU model": "M1", "Hard disk size": "2 TB"}}
]

NEGATIVE_DATA = [
    {"name": ["Apple MacBook Pro 16"], "data": {"year": 2019, "price": 1849.99,
                                                "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}},
    {"name": {"Apple MacBook Pro 19": ''}, "data": {"year": 2021, "price": 1849.99,
                                                    "CPU model": "M1", "Hard disk size": "2 TB"}}
]

PATCH_DATA = [
    {"name": "Apple MacBook Pro 11", "data": {"price": 2000.99, "CPU model": "Intel Core i9"}}
]


@pytest.mark.parametrize('data', TEST_DATA)
def test_post_a_new_object(create_post_endpoint, data):
    create_post_endpoint.create_new_post(payload=data)
    create_post_endpoint.check_response_status_code()
    create_post_endpoint.check_response_name_for_object(data['name'])


@pytest.mark.parametrize('data', NEGATIVE_DATA)
def test_post_with_array_in_title(create_post_endpoint, data):
    create_post_endpoint.create_new_post(payload=data)
    create_post_endpoint.check_bad_request()


@pytest.mark.parametrize('data', TEST_DATA)
def test_put_a_post(update_post_endpoint, create_post_endpoint, data):
    payload = {"name": "Apple MacBook Pro 24", "data": {"year": 2012, "price": 184.99,
                                                        "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}}
    response = create_post_endpoint.create_new_post(payload=data)
    update_post_endpoint.make_changes_in_post(response.json()['id'], payload)
    update_post_endpoint.check_response_status_code()
    update_post_endpoint.check_response_name_for_object(payload['name'])


@pytest.mark.parametrize('data', PATCH_DATA)
def test_patch_a_post(modify_post_endpoint, create_post_endpoint, data):
    payload = {"name": "Apple MacBook Pro 11", "data": {"price": 2000.99, "CPU model": "Intel Core i9"}}
    response = create_post_endpoint.create_new_post(payload=data)
    modify_post_endpoint.partial_update_in_post(response.json()['id'], payload)
    modify_post_endpoint.check_response_name_for_object(payload['name'])


@pytest.mark.parametrize('data', TEST_DATA)
def test_delete_a_post(delete_post_endpoint, create_post_endpoint, data):
    response = create_post_endpoint.create_new_post(payload=data)
    delete_post_endpoint.delete_post(response.json()['id'])
    delete_post_endpoint.check_response_status_code()
