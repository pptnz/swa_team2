from django import forms


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(label='Current Password', widget=forms.PasswordInput, min_length=8, max_length=30)
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput, min_length=8, max_length=30)
    new_password_check = forms.CharField(label='New Password Again', widget=forms.PasswordInput, min_length=8, max_length=30)
