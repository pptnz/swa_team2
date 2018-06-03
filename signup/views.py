from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
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

    # todo: change this default link
    if request.user.is_authenticated:
        return HttpResponseRedirect('/habitmaker/')

    if request.method == 'GET':
        sign_up_form = SignUpForm()
        return render(request, 'signup/signup.html', {'sign_up_form': sign_up_form})

    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            # sign-up wigh given data.
            form_data = sign_up_form.cleaned_data
            username = form_data['username']
            password = form_data['password']
            nickname = form_data['nickname']
            email = form_data['email']

            new_user = User.objects.create_user(username=username, password=password, first_name=nickname)
            CustomUser.objects.create(django_user=new_user, is_email_authenticated=False)

            # Send email if email is given.
            if len(email) != 0:
                # Email is given. Send verification email to the user.
                new_user.email = email
                new_user.save()

                # todo: send email

            # Try login with the new user.
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/habitmaker/')
            else:
                # An error occurred.
                return render(request, 'signup/signup.html', {'sign_up_form': sign_up_form})

        # form not valid.
        return render(request, 'signup/signup.html', {'sign_up_form': sign_up_form})
