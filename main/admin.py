from django.contrib import admin
from .models import Jobs

@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'job_type', 'Salary')
    search_fields = ('title', 'location', 'job_type')
    list_filter = ('job_type',)

    # Include the image upload in the form
    fields = ('title', 'Salary', 'description', 'location', 'job_type', 'image')
