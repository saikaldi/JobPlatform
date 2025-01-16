from django.contrib import admin
from django.urls import path, include
from jobs import views

app_name = 'jobs'

urlpatterns = [
    path('search/', views.jobs, name='jobs'),
]