from django.contrib.admin.widgets import AdminDateWidget, AdminSplitDateTime
from django.db import models
from signin.models import CustomUser


class ToDo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=14)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    repetition = models.BooleanField(default=False)
    repetition_start = models.DateField(null=True)
    repetition_end = models.DateField(null=True)
