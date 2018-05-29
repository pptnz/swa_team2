from django.shortcuts import render


# Create your views here.
def habit_list(request):
    return render(request, 'habit/habit_list.html', {})
