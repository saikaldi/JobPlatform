from django.db import models

class JobPosting(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    location = models.CharField(max_length=255)
    JOB_TYPES = [
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('contract', 'Contract'),
        ('freelance', 'Freelance'),
        ('internship', 'Internship'),
    ]
    job_type = models.CharField(max_length=50, choices=JOB_TYPES)
    salary = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    contact_email = models.EmailField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"
