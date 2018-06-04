from django.shortcuts import render
from .forms import FindPasswordForm


def find_password_page(request):
    find_password_form = FindPasswordForm()
    return render(request, 'findpassword/findpassword.html', {'find_password_form': find_password_form})
