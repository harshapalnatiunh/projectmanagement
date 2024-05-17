from django.test import TestCase, Client
from django.urls import reverse
import json

class PeopleViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_people_home_view(self):
        response = self.client.get(reverse('employee_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'people/home.html')

    def test_fetch_people_data_view(self):
        response = self.client.get(reverse('fetch_people_data'))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'error': 'Failed to fetch data from the API'}
        )

    # This test will pass only when the API is up and running
    # and returns the expected data
    def test_fetch_people_data_view_with_api_call(self):
        response = self.client.get(reverse('fetch_people_data'))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue('users' in data)
