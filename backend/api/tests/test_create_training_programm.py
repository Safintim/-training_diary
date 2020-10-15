from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import test

from training import models

User = get_user_model()


class CreateTrainingProgrammTest(test.APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='test@mail.ru', password='123123'
        )
        self.client.force_login(self.user)

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
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            models.TrainingProgramm.objects.first().title,
            data['title']
        )
        self.assertEqual(
            models.Exercise.objects.first().title,
            data['exercises'][0]['title']
        )
        self.assertTrue(
            models.TrainingProgramm.objects.filter(
                exercises__title=data['exercises'][0]['title']
            ).exists()
        )

    def test_update(self):
        # TODO test
        pass
