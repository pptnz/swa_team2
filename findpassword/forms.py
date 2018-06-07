from django import forms


class FindPasswordForm(forms.Form):
    username = forms.CharField(label='ID', min_length=3, max_length=15)
    email = forms.EmailField(label='이메일')
