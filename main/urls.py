from django.contrib import admin
from django.urls import path, include
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    # path('about/', views.about, name='about'),
    # path('more-designs/', views.more_designs, name='more_designs')


]