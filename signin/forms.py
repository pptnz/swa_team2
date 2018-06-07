from django import forms


class SignInForm(forms.Form):
    username = forms.CharField(label='ID', min_length=3, max_length=15)
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput, min_length=8, max_length=30)
