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
        data = {
            'title': 'Title',
            'description': 'Description',
            'exercises': [
                {
                    'title': 'Exercises'
                }
            ]
        }
        url = reverse('training_programms-list')
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
        training_data = {
            'title': 'Title',
            'description': 'Description',
        }
        exercise_data = {
            'title': 'Exercises'
        }
        training = models.TrainingProgramm.objects.create(
            **training_data,
            author=self.user
        )
        exercise = models.Exercise.objects.create(
            **exercise_data,
            user=self.user
        )
        training.exercises.add(exercise)

        data_not_id = {
            'exercises': [
                {
                    'title': 'Exercises213'
                }
            ]
        }
        url = reverse('training_programms-detail', args=[training.id])
        response1 = self.client.put(url, data_not_id, format='json')
        self.assertEqual(response1.status_code, 200)
        self.assertNotEqual(
            models.Exercise.objects.first().title,
            data_not_id['exercises'][0]['title'],
        )
        data_with_id = {
            'exercises': [
                {
                    'id': 1,
                    'title': 'Exercises213'
                }
            ]
        }
        response2 = self.client.put(url, data_with_id, format='json')
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(
            models.Exercise.objects.first().title,
            data_with_id['exercises'][0]['title'],
        )
