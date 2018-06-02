from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.Model):
    """
    Custom User model that includes 'is email authenticated' field.
    """
    django_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='custom_user')
    is_email_authenticated = models.BooleanField(default=False)

    def authenticate_email(self):
        self.is_email_authenticated = True
