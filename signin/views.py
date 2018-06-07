from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from .forms import SignInForm


@require_http_methods(['GET', 'POST'])
def sign_in_page(request):
    """
    Render sign-in page.

    - GET:
        - If already authenticated, redirect to next page.
        - If not, just render new form and return.

    - POST: trying to sign-in.
        - If form is not valid, do nothing.
        - If form is valid, try to authenticate.
            - If succeeded, redirect to next page.
            - If not, alert the user and do nothing.
    """

    # todo: change this default link
    next_page = '/habitmaker/'

    if request.user.is_authenticated:
        return HttpResponseRedirect(next_page)

    if request.method == 'GET':
        sign_in_form = SignInForm()
        return render(request, 'signin/signin.html', {'sign_in_form': sign_in_form})

    if request.method == 'POST':
        sign_in_form = SignInForm(request.POST)
        if sign_in_form.is_valid():
            username = sign_in_form.cleaned_data['username']
            password = sign_in_form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                # login succeeded
                login(request, user)

                # If redirected by other sites, user has different next page to redirect.
                if 'next' in request.GET:
                    next_page = request.GET['next']

                messages.success(request, '{}님, 환영합니다!'.format(user.first_name))
                return HttpResponseRedirect(next_page)

            # login failed.
            messages.error(request, '잘못된 ID나 비밀번호를 입력하셨습니다.')
            return render(request, 'signin/signin.html', {'sign_in_form': sign_in_form})

        # Form is not valid.
        return render(request, 'signin/signin.html', {'sign_in_form': sign_in_form})


@require_http_methods(['GET'])
def sign_in_redirect(request):
    """
    Redirect to sign-in page.
    """
    return HttpResponseRedirect("/sign_in/")
