from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habits
from users.models import User


class HabitsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test3@test.ru")
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        url = reverse('habits:habits_create')
        data = {
            "user": self.user,
            "place": "Парк",
            "time": "10:00:00",
            "action": "Выйти на пробежку",
            "frequency_habit": 1,
            "time_complete": "00:02:00"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(Habits.objects.count(), 1)
        # self.assertEqual(Habits.objects.get().action, 'Выйти на пробежку')
    #
    # def test_retrieve_habit(self):
    #     habit = Habits.objects.create(
    #         user=self.user,
    #         place="Парк",
    #         time="10:00:00",
    #         action="Выйти на пробежку",
    #         frequency_habit= 1,
    #         time_complete = "00:02:00"
    #     )
    #     url = reverse('habits:habits_retrieve', kwargs={'pk': habit.id})
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['action'], 'Выйти на пробежку')
    #
    # def test_update_habit(self):
    #     habit = Habits.objects.create(
    #         user=self.user,
    #         place="Парк",
    #         time="10:00:00",
    #         action="Выйти на пробежку",
    #         frequency_habit=1,
    #         time_complete = "00:02:00"
    #     )
    #     url = reverse('habits:habits_retrieve', kwargs={'pk': habit.id})
    #     data = {
    #         "user": self.user,
    #         "place": "Дома",
    #         "time": "10:00:00",
    #         "action": "Читать книгу",
    #         "frequency_habit": 1,
    #         "time_complete": "00:02:00"
    #     }
    #     response = self.client.put(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(Habits.objects.get().action, 'Читать книгу')
    #
    # def test_delete_habit(self):
    #     habit = Habits.objects.create(
    #         user=self.user,
    #         place="Парк",
    #         time="10:00:00",
    #         action="Выйти на пробежку",
    #         frequency_habit=1,
    #         time_complete="00:02:00"
    #     )
    #     url = reverse('habits:habits_retrieve', kwargs={'pk': habit.id})
    #     response = self.client.delete(url)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     self.assertEqual(Habits.objects.count(), 0)
    #
    # def test_list_public_habits(self):
    #     Habits.objects.create(
    #         user=self.user,
    #         place="Парк",
    #         time="10:00:00",
    #         action="Выйти на пробежку",
    #         frequency_habit=1,
    #         time_complete="00:02:00"
    #     )
    #     url = reverse('habits:public')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 1)
    #
    # def test_list_user_habits(self):
    #     Habits.objects.create(
    #         user=self.user,
    #         place="Парк",
    #         time="10:00:00",
    #         action="Выйти на пробежку",
    #         frequency_habit=1,
    #         time_complete="00:02:00"
    #     )
    #     url = reverse('habits:habits_list')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 1)
