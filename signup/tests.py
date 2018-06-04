from django.apps import apps
from django.test import TestCase
from .apps import SignupConfig
from signin.models import User, CustomUser


class SignUpTestCase(TestCase):
    def setUp(self):
        self.django_user = User.objects.create_user(username='testusername', password='testpassword')
        self.custom_user = CustomUser.objects.create(django_user=self.django_user)

    def test_apps(self):
        self.assertEqual(SignupConfig.name, 'signup')
        self.assertEqual(apps.get_app_config('signup').name, 'signup')

    def test_already_signed_in(self):
        self.client.login(username='testusername', password='testpassword')
        response = self.client.get('/sign_up/')
        self.assertRedirects(response, '/habitmaker/')

    def test_get(self):
        response = self.client.get('/sign_up/')
        self.assertEqual(response.status_code, 200)

    def test_post_form_not_valid(self):
        response = self.client.post('/sign_up/', {'username': 'wrongusername'})
        self.assertEqual(response.status_code, 200)

    def test_post_duplicated_user(self):
        response = self.client.post('/sign_up/',
                                    {'username': 'testusername', 'password': 'diffpassword', 'nickname': 'hello'})
        self.assertEqual(response.status_code, 200)

    def test_post_no_email(self):
        response = self.client.post('/sign_up/',
                                    {'username': 'diffusername', 'password': 'diffpassword', 'nickname': 'hello'})
        self.assertRedirects(response, '/habitmaker/')

    def test_post_email(self):
        response = self.client.post('/sign_up/',
                                    {'username': 'diffusername', 'password': 'diffpassword', 'nickname': 'hello',
                                     'email': 'abc@def.ghi'})
        self.assertRedirects(response, '/habitmaker/')

    def test_activate_fail(self):
        response = self.client.post('/sign_up/activate_email/AB/4ab-a10203e7ac2739a66329/')
        self.assertRedirects(response, '/sign_in/')