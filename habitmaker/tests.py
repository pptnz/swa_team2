from django.test import TestCase
from .models import Habit, SuccessCheck

# Create your tests here.
class HabitTestCase(TestCase):
    def setUp(self):
        Habit.objects.create(user=)
        user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
        title = models.CharField(max_length=30)

        created_date = models.DateField(default=timezone.now)
        success_days = models.PositiveIntegerField()
