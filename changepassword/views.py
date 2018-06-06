from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .forms import ChangePasswordForm


@login_required
@require_http_methods(['GET', 'POST'])
def change_password_page(request):
    """
        Render sign-in page.

        - GET:
            - If not signed in, redirect to sign in page.
            - If signed in, just render new form and return.

        - POST: trying to sign-in.
            - If form is not valid, do nothing.
            - If form is valid, try to change password
                - If password does not match, message user and do nothing.
                - If match, change password and redirect to main page.
        """
    if request.method == 'GET':
        change_password_form = ChangePasswordForm()
        return render(request, 'changepassword/change_password.html', {'change_password_form': change_password_form})

    # POST
    change_password_form = ChangePasswordForm(request.POST)

    if change_password_form.is_valid():
        form_data = change_password_form.cleaned_data
        current_password = form_data['current_password']
        new_password = form_data['new_password']
        new_password_check = form_data['new_password_check']

        if not request.user.check_password(current_password):
            messages.info(request, '현재 비밀번호가 일치하지 않습니다.')
            return render(request, 'changepassword/change_password.html',
                          {'change_password_form': change_password_form})

        if new_password != new_password_check:
            messages.info(request, '새로운 비밀번호가 일치하지 않습니다.')
            return render(request, 'changepassword/change_password.html',
                          {'change_password_form': change_password_form})

        if current_password == new_password:
            messages.info(request, '기존 비밀번호와 같은 비밀번호로 변경하실 수 없습니다.')
            return render(request, 'changepassword/change_password.html',
                          {'change_password_form': change_password_form})

        # change password
        request.user.set_password(new_password)
        request.user.save()
        update_session_auth_hash(request, request.user)
        messages.info(request, '비밀번호가 정상적으로 변경되었습니다.')
        return HttpResponseRedirect('/habitmaker/')

    # form is not valid
    return render(request, 'changepassword/change_password.html', {'change_password_form': change_password_form})
