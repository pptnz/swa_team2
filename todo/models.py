from django.db import models
from django.utils import timezone

class ToDo(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    repetition = models.BooleanField()
    repetition_period = models.DurationField

# Create your models here.
