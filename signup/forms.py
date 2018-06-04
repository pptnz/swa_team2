from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField(label='Username', min_length=3, max_length=15)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, min_length=8, max_length=30)
    nickname = forms.CharField(label='Nickname', min_length=3, max_length=15)
    email = forms.EmailField(label='Email (Optional)', required=False)
