# tracker/forms.py
from django import forms
from .models import Workout, Meal

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['exercise', 'duration']

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['name', 'calories']
