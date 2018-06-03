from django import forms


class HabitForm(forms.Form):
    habit = forms.CharField(label='', max_length=20, widget=forms.TextInput(attrs={'class': 'habit_form'}))
