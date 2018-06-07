from django import forms


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(label='현재 비밀번호', widget=forms.PasswordInput, min_length=6, max_length=30)
    new_password = forms.CharField(label='새 비밀번호', widget=forms.PasswordInput, min_length=6, max_length=30)
    new_password_check = forms.CharField(label='새 비밀번호 확인', widget=forms.PasswordInput,
                                         min_length=6, max_length=30)
