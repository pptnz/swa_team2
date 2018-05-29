from django.shortcuts import render


# Create your views here.
def habit_list(request):
    return render(request, 'habitmaker/habit_list.html', {})
