from django.urls import reverse
from rest_framework import test


class CreateTrainingProgrammTest(test.APITestCase):
    def test_create(self):
        url = reverse('training_programms-list')
        data = {
            'title': 'Title',
            'description': 'Description',
            'exercises': [
                {
                    'title': 'Exercises'
                }
            ]
        }
        response = self.client.post(url, data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, 201)
