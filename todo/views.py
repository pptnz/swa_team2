from django.shortcuts import render
from django.template.loader import render_to_string

from .models import ToDo
from .forms import ToDoForm


def todo(request):
    form = ToDoForm()
    header_bar = render_to_string('headerbar/headerbar.html', {'username': request.user.first_name})
    return render(request, 'todo/todo.html', {'form': form, 'header_bar': header_bar})


def add_new(request):
    form = ToDoForm()
    return render(request, 'todo_add/todo_add.html', {'form': form})