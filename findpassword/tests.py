from django.test import TestCase
from django.apps import apps
from .apps import FindpasswordConfig
from signin.models import User, CustomUser


class FindPasswordTestCase(TestCase):
    def setUp(self):
        self.django_user = User.objects.create_user(username='testusername', password='testpassword')
        self.custom_user = CustomUser.objects.create(django_user=self.django_user)
        self.django_user.email = 'test@test.com'
        self.django_user.save()
        self.custom_user.is_email_authenticated = True
        self.custom_user.save()

        self.no_email_django_user = User.objects.create_user(username='hihihi', password='12345678')
        self.no_email_custom_user = CustomUser.objects.create(django_user=self.no_email_django_user)

    def test_apps(self):
        self.assertEqual(FindpasswordConfig.name, 'findpassword')
        self.assertEqual(apps.get_app_config('findpassword').name, 'findpassword')

    def test_already_signed_in(self):
        self.client.login(username='testusername', password='testpassword')
        response = self.client.get('/find_password/')
        self.assertRedirects(response, '/habitmaker/')

    def test_get(self):
        response = self.client.get('/find_password/')
        self.assertEqual(response.status_code, 200)

    def test_post_form_not_valid(self):
        response = self.client.post('/find_password/', {'username': 'wrongusername'})
        self.assertEqual(response.status_code, 200)

    def test_post_no_user(self):
        response = self.client.post('/find_password/', {'username': 'nouser', 'email': 'email@email.com'})
        self.assertEqual(response.status_code, 200)

    def test_post_no_email_authenticated(self):
        response = self.client.post('/find_password/', {'username': 'hihihi', 'email': 'email@email.com'})
        self.assertEqual(response.status_code, 200)

    def test_post_different_email(self):
        response = self.client.post('/find_password/', {'username': 'testusername', 'email': 'email@email.com'})
        self.assertEqual(response.status_code, 200)

    def test_send_email(self):
        response = self.client.post('/find_password/', {'username': 'testusername', 'email': 'test@test.com'})
        self.assertRedirects(response, '/sign_in/')
