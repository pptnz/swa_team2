from django import forms


class HabitForm(forms.Form):
    habit = forms.CharField(label='', max_length=50)

