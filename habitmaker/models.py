from django.db import models
from django.utils import timezone
from signin.models import CustomUser


class Habit(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)

    created_date = models.DateField(default=timezone.now)
    success_days = models.PositiveIntegerField()

    def today_success(self):
        success = SuccessCheck.objects.all().filter(habit=self).filter(date=timezone.now())
        return success

    def create_success(self):
        self.success_days += 1
        self.save()
        SuccessCheck.objects.create(habit=self)

    def delete_success(self, success):
        self.success_days -= 1
        self.save()
        success.delete()

    def total_days(self):
        return (timezone.now().date() - self.created_date).days

    def success_rate(self):
        return "{:.0f}".format(100 * self.success_days / self.total_days())


class SuccessCheck(models.Model):
    habit = models.ForeignKey(Habit, null=False, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
