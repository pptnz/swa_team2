from django.test import TestCase
from django.apps import apps
from .apps import TodoConfig


class TodoTest(TestCase):
    def setUp(self):
        pass

    def test_apps(self):
        self.assertEqual(TodoConfig.name, 'todo')
        self.assertEqual(apps.get_app_config('todo').name, 'todo')