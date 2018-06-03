from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField(label='Username', max_length=15)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=30)
    nickname = forms.CharField(label='Nickname', max_length=10)
    email = forms.EmailField(label='Email (Optional)', required=False)
