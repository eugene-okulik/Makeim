import requests
import allure
from endpoints.endpoint import Endpoint


class ModifyPost(Endpoint):

    @allure.feature('API tests')
    @allure.story('Patch mtd')
    @allure.step('Modify a post')
    @allure.title('Внесение изменения методом PATCH')
    def partial_update_in_post(self, post_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'https://api.restful-api.dev/objects/{post_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
