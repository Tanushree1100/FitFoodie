from django.db import models

# tracker/models.py
from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    calories_burned_per_minute = models.FloatField()

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    duration = models.DurationField()

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length=100)
    calories = models.FloatField()
