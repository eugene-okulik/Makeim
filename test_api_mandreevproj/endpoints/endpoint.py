import allure


class Endpoint:
    url = 'https://api.restful-api.dev/objects'
    response = None
    json = None
    headers = {'Content-type': 'application/json'}

    @allure.step('Check name is correct')
    def check_response_name_for_object(self, name):
        assert self.response.json()['name'] == name, 'title is not title'

    @allure.step('Check status code = 200 of request to create')
    def check_response_status_code(self):
        assert self.response.status_code == 200, '200 is not 200'

