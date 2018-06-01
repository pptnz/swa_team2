from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Habit


# Create your views here.
@login_required
def habit_list(request):
    # After implement Sign-in
    # habits = Habit.objects.filter(user=request.user).order_by('created_date')
    habits = Habit.objects.all()
    return render(request, 'habitmaker/habit_list.html', {'habits': habits})
