import random
import string

from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.http import require_http_methods
from signin.models import User, CustomUser
from .forms import FindPasswordForm


def random_password(length=8):
    """
    Generate a random password, containing lowercase, uppercase and digit.

    :param length: length of the password to generate
    :return: generated password of given length
    """
    result_password = ""
    character_set = string.ascii_uppercase + string.ascii_lowercase + string.digits
    for _ in range(length):
        result_password += random.choice(character_set)
    return result_password


@require_http_methods(['GET', 'POST'])
def find_password_page(request):
    """
    Render find-password page.

    - Get:
        - If already signed in, redirect to next page.
        - If not, render the page.

    - Post: trying to find-password.
        - If form is not valid, do nothing.
        - If form is valid, check the user exists.
            - If exist, send email.
            - If not, do nothing.
    """
    if request.user.is_authenticated:
        return HttpResponseRedirect('/habitmaker/')

    if request.method == 'GET':
        find_password_form = FindPasswordForm()
        return render(request, 'findpassword/findpassword.html', {'find_password_form': find_password_form})

    find_password_form = FindPasswordForm(request.POST)

    if find_password_form.is_valid():
        # check user exists.
        form_data = find_password_form.cleaned_data
        username = form_data['username']
        email = form_data['email']

        try:
            django_user = User.objects.get(username=username)
            custom_user = CustomUser.objects.get(django_user=django_user)
        except User.DoesNotExist:
            messages.error(request, '존재하지 않는 ID입니다.')
            return render(request, 'findpassword/findpassword.html', {'find_password_form': find_password_form})

        if not custom_user.is_email_authenticated:
            messages.error(request, '이메일이 등록되지 않은 ID입니다. 비밀번호 찾기가 불가능합니다.')
            return render(request, 'findpassword/findpassword.html', {'find_password_form': find_password_form})

        if django_user.email != email:
            messages.error(request, 'ID에 등록된 이메일과 다른 이메일을 입력하셨습니다.')
            return render(request, 'findpassword/findpassword.html', {'find_password_form': find_password_form})

        # send email
        temp_password = random_password()
        django_user.set_password(temp_password)
        django_user.save()
        mail_subject = 'Momentum: 임시 비밀번호를 보내드립니다.'
        message = render_to_string('findpassword/temp_password_email.html', {
            'nickname': django_user.first_name,
            'temp_password': temp_password
        })
        email = EmailMessage(
            mail_subject, message, to=[email]
        )
        email.send()

        # Redirect to main page
        messages.info(request, '이메일로 임시 비밀번호를 전송했습니다.')
        return HttpResponseRedirect('/sign_in/')

    # form is not valid.
    return render(request, 'findpassword/findpassword.html', {'find_password_form': find_password_form})
