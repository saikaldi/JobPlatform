from django.contrib import admin
from .models import JobPosting

@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'job_type', 'posted_at')
    search_fields = ('title', 'company', 'location', 'job_type')
    list_filter = ('job_type', 'posted_at')
