import json

from django.test import TestCase, Client
from .models import Habit, SuccessCheck
from signin.models import User, CustomUser


# Create your tests here.
class HabitTestCase(TestCase):
    def setUp(self):
        self.django_user = User.objects.create_user(username='testusername', password='testpassword')
        self.custom_user = CustomUser.objects.create(django_user=self.django_user)
        self.custom_user.save()

        self.habit1 = Habit(user=self.custom_user, title='read books', created_date='2018-01-02', success_days=1)
        self.habit2 = Habit(user=self.custom_user, title='do exercise', created_date='2018-05-06', success_days=2)
        self.habit3 = Habit(user=self.custom_user, title='study english', created_date='2018-03-31', success_days=1)
        self.habit1.save()
        self.habit2.save()
        self.habit3.save()

        self.success_check1 = SuccessCheck(habit=self.habit1, date='2018-04-03')
        self.success_check2 = SuccessCheck(habit=self.habit2, date='2018-05-08')
        self.success_check3 = SuccessCheck(habit=self.habit2, date='2018-06-01')
        self.success_check4 = SuccessCheck(habit=self.habit3, date='2018-03-03')
        self.success_check1.save()
        self.success_check2.save()
        self.success_check3.save()
        self.success_check4.save()

        self.client = Client()

    def test_habit_list_get(self):
        response1 = self.client.post('/sign_in/', {'username': 'testusername', 'password': 'testpassword'})
        self.assertRedirects(response1, '/habitmaker/')

        response = self.client.get('/habitmaker/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'read books')
        self.assertContains(response, 'do exercise')
        self.assertContains(response, 'study english')

    def test_habit_list_post(self):
        response1 = self.client.post('/sign_in/', {'username': 'testusername', 'password': 'testpassword'})
        self.assertRedirects(response1, '/habitmaker/')

        response = self.client.post('/habitmaker/',
                                    {'habit': "be happy"})
        self.assertRedirects(response, '/habitmaker/')

        response = self.client.get('/habitmaker/')
        self.assertContains(response, 'be happy')

    def test_habit_list_invalid_post(self):
        response1 = self.client.post('/sign_in/', {'username': 'testusername', 'password': 'testpassword'})
        self.assertRedirects(response1, '/habitmaker/')

        response = self.client.post('/habitmaker/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'read books')

    def test_toggle_success_post(self):
        response = self.client.post('/habitmaker/toggle_success/',
                                    {'pk': self.habit1.pk}
                                    )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode())
        self.assertEqual(data['success_days'], 2)
        self.assertEqual(data['is_created'], 1)

        response = self.client.post('/habitmaker/toggle_success/',
                                    {'pk': self.habit1.pk},
                                    format='multipart'
                                    )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode())
        self.assertEqual(data['success_days'], 1)
        self.assertEqual(data['is_created'], 0)
