from django import forms


class SignInForm(forms.Form):
    username = forms.CharField(label='Username', max_length=15)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=30)
