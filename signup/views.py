import sqlite3

from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login
from django.db.utils import IntegrityError

from .tokens import account_activation_token
from .forms import SignUpForm
from signin.models import User, CustomUser


@require_http_methods(['GET', 'POST'])
def sign_up_page(request):
    """
    Render sign-up page.

    - Get:
        - If already signed in, redirect to next page.
        - If not, render the page.

    - Post: trying to sign-up.
        - If form is not valid, do nothing.
        - If form is valid, do sign-up.
            - If succeeded, redirect to next page.
            - If not, do nothing.
    """

    if request.user.is_authenticated:
        return HttpResponseRedirect('/habitmaker/')

    if request.method == 'GET':
        sign_up_form = SignUpForm()
        return render(request, 'signup/signup.html', {'sign_up_form': sign_up_form})

    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            # sign-up with given data.
            form_data = sign_up_form.cleaned_data
            username = form_data['username']
            password = form_data['password']
            password_check = form_data['password_check']
            nickname = form_data['nickname']
            email = form_data['email']

            if password != password_check:
                messages.info(request, '비밀번호가 일치하지 않습니다.')
                return render(request, 'signup/signup.html', {'sign_up_form': sign_up_form})

            # check if duplicated user exists.
            try:
                new_user = User.objects.create_user(username=username, password=password, first_name=nickname)
                CustomUser.objects.create(django_user=new_user, is_email_authenticated=False)
            except (sqlite3.IntegrityError, IntegrityError):
                # username is duplicated
                messages.info(request, '이미 존재하는 ID입니다. 다른 ID를 사용해주세요.')
                return render(request, 'signup/signup.html', {'sign_up_form': sign_up_form})

            # Send email if email is given.
            if len(email) != 0:
                # Email is given. Send verification email to the user.
                new_user.email = email
                new_user.save()

                current_site = get_current_site(request)
                mail_subject = '아구아구: 이메일을 인증해주세요.'
                message = render_to_string('signup/verification_email.html', {
                    'nickname': nickname,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(new_user.pk)).decode(),
                    'token': account_activation_token.make_token(new_user),
                })
                email = EmailMessage(
                    mail_subject, message, to=[email]
                )
                email.send()

            # Try login with the new user.
            login(request, new_user)
            messages.info(request, '회원가입이 완료되었습니다!')
            return HttpResponseRedirect('/habitmaker/')

        # form not valid.
        return render(request, 'signup/signup.html', {'sign_up_form': sign_up_form})


def activate_email(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        django_user = User.objects.get(pk=uid)
        custom_user = django_user.custom_user
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        messages.info(request, '인증 오류가 발생하였습니다.')
        return HttpResponseRedirect('/sign_in/')

    if account_activation_token.check_token(django_user, token):
        custom_user.authenticate_email()
        custom_user.save()
        messages.info(request, '성공적으로 인증되었습니다.')
        return HttpResponseRedirect('/sign_in/')
    else:
        messages.info(request, '인증 오류가 발생하였습니다.')
        return HttpResponseRedirect('/sign_in/')
