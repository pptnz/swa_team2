import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.http import require_http_methods

from .models import ToDo
from .forms import ToDoForm


@login_required
def todo(request):
    header_bar = render_to_string('headerbar/headerbar.html', {'username': request.user.first_name})
    todo_list = ToDo.objects.filter(user=request.user.custom_user)
    return render(request, 'todo/todo.html', {'header_bar': header_bar, 'todo': todo_list })

@login_required
@require_http_methods(['GET', 'POST'])
def post_todo(request):
    if request.method == 'GET':
        form = ToDoForm()
        header_bar = render_to_string('headerbar/headerbar.html', {'username': request.user.first_name})
        return render(request, 'todo/post_todo.html', {'form': form, 'header_bar': header_bar})

    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            user = request.user.custom_user
            title = form.cleaned_data['title']
            date = form.cleaned_data['date']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            repetition = form.cleaned_data['repetition']
            repetition_start = form.cleaned_data['repetition_start']
            repetition_end = form.cleaned_data['repetition_end']

            if start_time > end_time:
                messages.error(request, '시작하는 시각이 끝나는 시각보다 작아야 합니다')
            elif repetition and not (repetition_start <= date <= repetition_end):
                messages.error(request, '날짜가 반복 기간 안에 있어야 합니다')
            if start_time < datetime.datetime(2000, 1, 1, 7, 0, 0).time():
                messages.error(request, '시간을 07:00에서 23:59까지로 설정할 수 있습니다')

            # Form is valid
            else:
                if not repetition:
                    repetition_start = None
                    repetition_end = None
                todo = ToDo(user=user, title=title, date=date, start_time=start_time,
                            end_time=end_time, repetition=repetition,
                            repetition_start=repetition_start, repetition_end=repetition_end)
                todo.save()
                return HttpResponseRedirect('/todo/')

        # Form is not valid
        header_bar = render_to_string('headerbar/headerbar.html', {'username': request.user.first_name})
        return render(request, 'todo/post_todo.html', {'form': form, 'header_bar': header_bar})
