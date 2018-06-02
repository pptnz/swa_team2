import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required

from .models import Habit, SuccessCheck
from django.utils import timezone


# Create your views here.
@login_required
@require_GET
def habit_list(request):
    # After implement Sign-in
    # habits = Habit.objects.filter(user=request.user).order_by('created_date')
    habits = Habit.objects.all()
    return render(request, 'habitmaker/habit_list.html', {'habits': habits})


@require_POST
def toggle_success(request):
    pk = request.POST.get('pk', None)
    habit = get_object_or_404(Habit, pk=pk)

    success = habit.today_success()

    if success.count() == 0:
        habit.create_success()
        success_rate = habit.success_rate()
        context = {'success_rate': success_rate, 'success_days': habit.success_days, 'is_created': 1}
    else:
        habit.delete_success(success)
        success_rate = habit.success_rate()
        context = {'success_rate': success_rate, 'success_days': habit.success_days, 'is_created': 0}

    return HttpResponse(json.dumps(context), content_type="application/json")
