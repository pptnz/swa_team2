from django.db import models
from django.utils import timezone


class Habit(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now    )

    success_days = models.PositiveIntegerField()

    def check_success(self):
        self.success_days += 1
        SuccessCheck.objects.create(habit=self, date=timezone.now)

    def total_days(self):
        return (timezone.now().date() - self.created_date.date()).days

    def success_rate(self):
        return "{:.3f}".format(100 * self.success_days / self.total_days())


class SuccessCheck(models.Model):
    habit = models.ForeignKey(Habit, null=False, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

