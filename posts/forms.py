from django import forms
from .models import JobPosting

class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = ['title', 'company', 'logo', 'location', 'job_type', 'salary', 'description', 'contact_email']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Describe the job'}),
            'title': forms.TextInput(attrs={'placeholder': 'Job Title'}),
            'company': forms.TextInput(attrs={'placeholder': 'Company Name'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
            'salary': forms.TextInput(attrs={'placeholder': 'Salary Range'}),
            'contact_email': forms.EmailInput(attrs={'placeholder': 'Contact Email'}),
            'job_type': forms.Select(attrs={'class': 'form-select'}),
        }
