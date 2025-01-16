from django.shortcuts import render

from posts.models import JobPosting


# Create your views here.


def jobs(request):
    jobs = JobPosting.objects.all()
    return render(request, "jobs/job_find.html", {'jobs':jobs})
