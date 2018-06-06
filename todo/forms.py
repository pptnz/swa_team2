from django import forms
from django.contrib.admin.widgets import AdminTimeWidget

from .models import ToDo

class ToDoForm(forms.Form):
    title = forms.CharField(label='일정 제목', max_length=20,
                            widget=forms.TextInput(attrs={'class': 'todo_form'}))
    date = forms.DateField(label='날짜', widget=forms.SelectDateWidget)
    start_time = forms.TimeField(label='시작 시각', widget=AdminTimeWidget(format='%H:%M'))
    end_time = forms.TimeField(label='끝 시각', widget=forms.TimeInput)
    repetition = forms.BooleanField(label='매주 반복')
    repeat_start = forms.DateField(label='반복 시작 날짜', widget=forms.SelectDateWidget)
    repeat_end = forms.DateField(label='반복 끝 날짜', widget=forms.SelectDateWidget)

