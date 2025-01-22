from django.contrib import admin

from jobs.models import JobApplication


# Register your models here.

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'name', 'email', 'applied_at')