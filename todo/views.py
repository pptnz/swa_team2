from django.shortcuts import render
from .models import ToDo
from .forms import ToDoForm

# Create your views here.
def todo(request):
    form = ToDoForm()
    return render(request, 'todo/todo.html', {'form': form})

def add_new(request):
    form = ToDoForm()
    return render(request, 'todo_add/todo_add.html', {'form': form})