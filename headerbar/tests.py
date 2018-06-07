from django.apps import apps
from django.test import TestCase
from .apps import HeaderbarConfig
from signin.models import User, CustomUser


class HeaderBar(TestCase):
    def setUp(self):
        self.django_user = User.objects.create_user(username='testusername', password='testpassword')
        self.custom_user = CustomUser.objects.create(django_user=self.django_user)

    def test_apps(self):
        self.assertEqual(HeaderbarConfig.name, 'headerbar')
        self.assertEqual(apps.get_app_config('headerbar').name, 'headerbar')

    def test_logout(self):
        self.client.login(username='testusername', password='testpassword')
        response = self.client.get('/sign_out/')
        self.assertRedirects(response, '/sign_in/')
