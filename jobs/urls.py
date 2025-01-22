from django.contrib import admin
from django.urls import path, include
from jobs import views

app_name = 'jobs'

urlpatterns = [
    path('all/', views.jobs, name='jobs'),
    path('<int:pk>/', views.job_detail, name='job_detail'),
    path('<int:pk>/apply/', views.apply_for_job, name='apply_job'),
    path('save-job/<int:job_id>/', views.save_job, name='save_job'),
    path('search-results/', views.search_results, name='search_results'),
]