from django import forms


class SignInForm(forms.Form):
    username = forms.CharField(label='Username', min_length=3, max_length=15)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, min_length=8, max_length=30)

