from django.test import TestCase
from django.apps import apps
from .apps import ChangepasswordConfig
from signin.models import User, CustomUser


class FindPasswordTestCase(TestCase):
    def setUp(self):
        self.django_user = User.objects.create_user(username='testusername', password='testpassword')
        self.custom_user = CustomUser.objects.create(django_user=self.django_user)

    def test_apps(self):
        self.assertEqual(ChangepasswordConfig.name, 'changepassword')
        self.assertEqual(apps.get_app_config('changepassword').name, 'changepassword')

    def test_get_not_signed_in(self):
        response = self.client.get('/change_password/')
        self.assertRedirects(response, '/sign_in/?next=/change_password/')

    def test_get(self):
        self.client.login(username='testusername', password='testpassword')
        response = self.client.get('/change_password/')
        self.assertEqual(response.status_code, 200)

    def test_post_form_not_valid(self):
        self.client.login(username='testusername', password='testpassword')
        response = self.client.post('/change_password/', {'current_password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)

    def test_post_not_matching_current_password(self):
        self.client.login(username='testusername', password='testpassword')
        response = self.client.post('/change_password/',
                                    {'current_password': 'wrongpassword',
                                     'new_password': '11111111',
                                     'new_password_check': '11111111'})
        self.assertEqual(response.status_code, 200)

    def test_post_not_matching_new_password(self):
        self.client.login(username='testusername', password='testpassword')
        response = self.client.post('/change_password/',
                                    {'current_password': 'testpassword',
                                     'new_password': '22222222',
                                     'new_password_check': '11111111'})
        self.assertEqual(response.status_code, 200)

    def test_post_same_password(self):
        self.client.login(username='testusername', password='testpassword')
        response = self.client.post('/change_password/',
                                    {'current_password': 'testpassword',
                                     'new_password': 'testpassword',
                                     'new_password_check': 'testpassword'})
        self.assertEqual(response.status_code, 200)

    def test_successful_change(self):
        self.client.login(username='testusername', password='testpassword')
        response = self.client.post('/change_password/',
                                    {'current_password': 'testpassword',
                                     'new_password': 'newpassword',
                                     'new_password_check': 'newpassword'})
        self.assertRedirects(response, '/habitmaker/')
