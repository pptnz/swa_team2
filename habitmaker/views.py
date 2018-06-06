from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.views.decorators.http import require_GET, require_http_methods

from signin.models import CustomUser
from .forms import HabitForm
from .models import Habit


# Create your views here.
@login_required
@require_http_methods(['GET', 'POST'])
def habit_list(request):
    if request.method == 'GET':
        # habits = Habit.objects.filter(user=request.user).order_by('created_date')
        habits = Habit.objects.order_by('created_date')
        habit_form = HabitForm()
        header_bar = render_to_string('headerbar/headerbar.html', {'username': request.user.first_name})
        return render(request, 'habitmaker/habit_list.html', {'habits': habits, 'habit_form': habit_form,
                                                              'header_bar': header_bar})

    elif request.method == 'POST':
        habit_form = HabitForm(request.POST)
        if habit_form.is_valid():
            title = habit_form.cleaned_data['habit']

            # habit = Habit(user=request.user, title=title)
            habit = Habit(user=CustomUser.objects.get(pk=1), title=title)
            habit.save()
            return HttpResponseRedirect('/habitmaker/')

        # Form is not valid.
        habits = Habit.objects.order_by('created_date')
        header_bar = render_to_string('headerbar/headerbar.html', {'username': request.user.first_name})
        return render(request, 'habitmaker/habit_list.html', {'habits': habits, 'habit_form': habit_form,
                                                              'header_bar': header_bar})


@require_GET
def toggle_success(request, pk):
    habit = get_object_or_404(Habit, pk=pk)

    success = habit.today_success()

    if success.count() == 0:
        habit.create_success()

    else:
        habit.delete_success(success)
    return HttpResponseRedirect('/habitmaker/')
