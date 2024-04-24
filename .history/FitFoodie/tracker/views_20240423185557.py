# tracker/views.py
from django.shortcuts import render, redirect
from .forms import WorkoutForm, MealForm
from .models import Workout, Meal
from django.contrib.auth.decorators import login_required

@login_required
def log_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('log_workout')  # Redirect to the same page after logging the workout
    else:
        form = WorkoutForm()
    return render(request, 'log_workout.html', {'form': form})

@login_required
def log_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            meal = form.save(commit=False)
            meal.user = request.user
            meal.save()
            return redirect('log_meal')  # Redirect to the same page after logging the meal
    else:
        form = MealForm()
    return render(request, 'log_meal.html', {'form': form})
