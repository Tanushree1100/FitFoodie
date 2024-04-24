# tracker/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('log-workout/', views.log_workout, name='log_workout'),
    path('log-meal/', views.log_meal, name='log_meal'),
]
