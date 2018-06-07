from django.test import TestCase, Client
from django.apps import apps
from .apps import TodoConfig
from signin.models import User, CustomUser
from .models import ToDo


class TodoTestCase(TestCase):
    def setUp(self):
        self.django_user = User.objects.create_user(username='testusername', password='testpassword')
        self.custom_user = CustomUser.objects.create(django_user=self.django_user)
        self.custom_user.save()

        self.todo1 = ToDo(user=self.custom_user, title='SW Application', date='2018-06-08', start_time='10:00',
                          end_time='13:00', repetition=True, repetition_start='2018-03-01', repetition_end='2018-06-08')
        self.todo2 = ToDo(user=self.custom_user, title='System Programming', date='2018-06-04', start_time='14:00',
                          end_time='15:30', repetition=True, repetition_start='2018-03-01', repetition_end='2018-06-08')
        self.todo3 = ToDo(user=self.custom_user, title='Proxy Lab', date='2018-06-06', start_time='16:00',
                          end_time='17:00', repetition=False, repetition_start=None, repetition_end=None)

        self.todo1.save()
        self.todo2.save()
        self.todo3.save()

        self.client = Client()

    def test_apps(self):
        self.assertEqual(TodoConfig.name, 'todo')
        self.assertEqual(apps.get_app_config('todo').name, 'todo')

    def test_todo_get(self):
        self.client.post('/sign_in/', {'username': 'testusername', 'password': 'testpassword'})

        response = self.client.get('/todo/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'SW Application')
        self.assertContains(response, 'System Programming')
        self.assertContains(response, 'Proxy Lab')

    def test_post_todo_get(self):
        self.client.post('/sign_in/', {'username': 'testusername', 'password': 'testpassword'})

        response = self.client.get('/todo/post/')
        self.assertEqual(response.status_code, 200)


    def test_post_todo_post_not_filled(self):
        self.client.post('/sign_in/', {'username': 'testusername', 'password': 'testpassword'})

        response = self.client.post('/todo/post/', {'title': "peppertones concert", 'date': '2018-06-09',
                                                    'start_time': '18:00', 'end_time': '21:00', 'repetition': False})
        self.assertEqual(response.status_code, 200)

    def test_post_todo_post_start_time_invalid(self):
        self.client.post('/sign_in/', {'username': 'testusername', 'password': 'testpassword'})

        response = self.client.post('/todo/post/', {'title': "peppertones concert", 'date': '2018-06-09',
                                                    'start_time': '22:00', 'end_time': '21:00', 'repetition': False,
                                                    'repetition_start': '2018-06-09', 'repetition_end': '2018-06-09'})
        self.assertEqual(response.status_code, 200)

    def test_post_todo_post_repetition_invalid(self):
        self.client.post('/sign_in/', {'username': 'testusername', 'password': 'testpassword'})

        response = self.client.post('/todo/post/', {'title': "pptnzconcert", 'date': '2018-06-09',
                                                    'start_time': '18:00', 'end_time': '21:00', 'repetition': True,
                                                    'repetition_start': '2018-06-07', 'repetition_end': '2018-06-08'})
        self.assertEqual(response.status_code, 200)


    def test_post_todo_post_repetition(self):
        self.client.post('/sign_in/', {'username': 'testusername', 'password': 'testpassword'})

        response = self.client.post('/todo/post/', {'title': "pptnzconcert", 'date': '2018-06-09',
                                                    'start_time': '18:00', 'end_time': '21:00', 'repetition': True,
                                                    'repetition_start': '2018-06-07', 'repetition_end': '2018-06-10'})
        self.assertRedirects(response, '/todo/')

        response = self.client.get('/todo/')
        self.assertContains(response, 'pptnzconcert')

    def test_post_todo_put(self):
        self.client.post('/sign_in/', {'username': 'testusername', 'password': 'testpassword'})

        response = self.client.put('/todo/post/')
        self.assertEqual(response.status_code, 405)
