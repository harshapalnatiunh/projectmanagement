from django.test import TestCase, Client
from django.urls import reverse
from .models import project
from .forms import ProjectEditForm

class AddProjectViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_add_project_view(self):
        # Define the form data to be sent in the POST request
        form_data = {
            'name': 'Test Project',
            'project_id': 'test_id',
            'project_status': True
        }

        # Send a POST request to the add_project view
        response = self.client.post(reverse('add_project'), form_data)

        # Check if the project was added successfully (HTTP status code 302 indicates a redirect)
        self.assertEqual(response.status_code, 302)

        # Check if the project was actually created in the database
        self.assertTrue(project.objects.filter(name='Test Project', project_id='test_id', project_status=True).exists())
