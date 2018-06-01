from django.shortcuts import render
from .forms import SignInForm


# Create your views here.
def sign_in_page(request):
    if request.method != 'POST':
        sign_in_form = SignInForm()
    else:
        sign_in_form = SignInForm(request.POST)
        if sign_in_form.is_valid():
            # Do Something
            print(sign_in_form.cleaned_data['username'])
            print(sign_in_form.cleaned_data['password'])

    return render(request, 'signin/signin.html', {'sign_in_form': sign_in_form})
