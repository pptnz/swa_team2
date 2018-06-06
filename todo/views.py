from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.template.loader import render_to_string
from signin.models import CustomUser
from .models import ToDo
from .forms import ToDoForm


def todo(request):
    pass


def post_todo(request):
    if request.method == 'GET':
        form = ToDoForm()
        header_bar = render_to_string('headerbar/headerbar.html', {'username': request.user.first_name})
        return render(request, 'todo/todo.html', {'form': form, 'header_bar': header_bar})

    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            # user = request.user
            user = CustomUser.objects.get(pk=1)
            title = form.cleaned_data['title']
            date = form.cleaned_data['date']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            repetition = form.cleaned_data['repetition']
            repetition_start = form.cleaned_data['repetition_start']
            repeat_end = form.cleaned_data['repeat_end']

            todo = ToDo(user=user, title=title, date=date, start_time=start_time,
                        end_time=end_time, repetition=repetition,
                        repetition_start=repetition_start, repeat_end=repeat_end)
            todo.save()
            return HttpResponseRedirect('/todo/')

        # Form is not valid
        header_bar = render_to_string('headerbar/headerbar.html', {'username': request.user.first_name})
        return render(request, 'todo/post_todo.html', {'form': form, 'header_bar': header_bar})
