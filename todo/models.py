from django.db import models
from django.utils import timezone

class ToDo(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=20)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    repetition = models.BooleanField()
    repetition_period = models.IntegerField()
    repeat_until = models.DateField()
# Create your models here.
