from django import forms
from django.contrib.admin.widgets import AdminTimeWidget
from django.utils import timezone

from .models import ToDo

class ToDoForm(forms.Form):
    title = forms.CharField(label='일정 제목', max_length=12,
                            widget=forms.TextInput(attrs={'class': 'todo_form'}))
    date = forms.DateField(label='날짜', widget=forms.SelectDateWidget, initial=timezone.now().date())
    start_time = forms.TimeField(label='시작 시각', widget=AdminTimeWidget(format="%H:%M", attrs={'placeholder': "HH:MM"}), initial=timezone.now().time())
    end_time = forms.TimeField(label='끝 시각', widget=AdminTimeWidget(format="%H:%M", attrs={'placeholder': "HH:MM"}), initial=timezone.now().time())
    repetition = forms.BooleanField(label='매주 반복', required=False)
    repetition_start = forms.DateField(label='반복 시작 날짜', widget=forms.SelectDateWidget, initial=timezone.now().date())
    repetition_end = forms.DateField(label='반복 끝 날짜', widget=forms.SelectDateWidget, initial=timezone.now().date())

