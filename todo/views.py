from django.shortcuts import render
from .models import ToDo

# Create your views here.
def todo_add(request):
    return render(request, 'todo_add/todo_add.html', {})
