from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from .forms import SignUpForm


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
    next_page = '/habitmaker/'

    if request.user.is_authenticated:
        return HttpResponseRedirect(next_page)

    if request.method == 'GET':
        sign_up_form = SignUpForm()
        return render(request, 'signup/signup.html', {'sign_up_form': sign_up_form})

    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            data = sign_up_form.cleaned_data
            print(data['username'], data['password'], data['nickname'], data['email'])
            return render(request, 'signup/signup.html', {'sign_up_form': sign_up_form})

        # form not valid.
        return render(request, 'signup/signup.html', {'sign_up_form': sign_up_form})
