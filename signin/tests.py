import json

from django.test import TestCase
from django.contrib.auth.models import User
from .models import CustomUser


class SignInTest(TestCase):
    def setUp(self):
        self.django_user = User.objects.create_user(username='testusername', password='testpassword')
        self.custom_user = CustomUser.objects.create(django_user=self.django_user)

    def test_sign_in_redirect_page(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/sign_in/')

    def test_get(self):
        response = self.client.get('/sign_in/')
        self.assertEqual(response.status_code, 200)

    def test_wrong_username(self):
        response = self.client.post('/sign_in/', {'username': 'wrongusername', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)

    def test_wrong_password(self):
        response = self.client.post('/sign_in/', {'username': 'testusername', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.post('/sign_in/', {'username': 'testusername', 'password': 'testpassword'})
        self.assertRedirects(response, '/habitmaker/')

    # todo: change this link
    def test_login_other_page(self):
        response = self.client.post('/sign_in/?next=/habitmaker/', {'username': 'testusername', 'password': 'testpassword'})
        self.assertRedirects(response, '/habitmaker/')

    def test_form_not_valid(self):
        response = self.client.post('/sign_in/', {'username': 'testusername'})
        self.assertEqual(response.status_code, 200)

    def test_email_verification(self):
        self.custom_user.authenticate_email()
        self.assertTrue(self.custom_user.is_email_authenticated)

    def test_already_signed_in(self):
        self.client.login(username='testusername', password='testpassword')
        response = self.client.get('/sign_in/')
        self.assertRedirects(response, '/habitmaker/')
