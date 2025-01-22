from django.db import models
from django.contrib.auth.models import User  # Assuming you have user authentication


# class Jobs(models.Model):
#
#     JOB_TYPE_CHOICES = [
#         ('part-time', 'Part-time'),
#         ('full-time', 'Full-time')
#     ]
#
#     title = models.CharField(max_length=255)
#     icon = models.ImageField(upload_to='icons/', blank=True, null=True)
#     Salary = models.FloatField()
#     description = models.TextField()
#     location = models.CharField(max_length=255)
#     job_type = models.CharField(max_length=255, choices=JOB_TYPE_CHOICES, default='full-time')
#
#     class Meta:
#         db_table = "job"
#         verbose_name = "Job"
#         verbose_name_plural = "Jobs"
#
#     def __str__(self):
#         return self.title