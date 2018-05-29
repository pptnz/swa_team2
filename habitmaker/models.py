from django.db import models
from django.utils import timezone


class Habit(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now)
