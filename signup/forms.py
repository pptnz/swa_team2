from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField(label='ID', min_length=3, max_length=15)
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput, min_length=6, max_length=30)
    password_check = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput, min_length=6, max_length=30)
    nickname = forms.CharField(label='닉네임', min_length=2, max_length=15)
    email = forms.EmailField(label='이메일 (선택)', required=False, help_text='이메일은 비밀번호 찾기에만 사용됩니다.')
