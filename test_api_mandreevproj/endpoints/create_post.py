import requests
import allure
from endpoints.endpoint import Endpoint


class CreatePost(Endpoint):

    @allure.step('Create new post')
    def create_new_post(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response

    @allure.step('Check 400 error')
    def check_bad_request(self):
        assert self.response.status_code == 400, '400 is not 400'
