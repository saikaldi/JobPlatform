from django import forms
from .models import JobPosting

class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = ['title', 'company', 'logo', 'location', 'job_type', 'salary', 'description', 'contact_email']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }
