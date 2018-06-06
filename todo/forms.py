from django import forms

from .models import ToDo

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('title','date','start_time','end_time','repetition','repetition_period','repeat_until')