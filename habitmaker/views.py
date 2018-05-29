from django.shortcuts import render
from .models import Habit


# Create your views here.
def habit_list(request):
    # After implement Sign-in
    # habits = Habit.objects.filter(user=request.user).order_by('created_date')
    habits = Habit.objects.all()
    return render(request, 'habitmaker/habit_list.html', {'habits': habits})
