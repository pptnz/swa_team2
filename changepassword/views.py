from django.shortcuts import render
from .forms import ChangePasswordForm


def change_password_page(request):
    change_password_form = ChangePasswordForm()
    return render(request, 'changepassword/change_password.html', {'change_password_form': change_password_form})