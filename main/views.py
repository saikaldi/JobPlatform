from django.shortcuts import render
# from main.models import Jobs
from jobs.models import JobPosting
from django.core.paginator import Paginator



# Create your views here.


def index(request):
    jobs = JobPosting.objects.all().order_by('-posted_at')
    paginator = Paginator(jobs, 3)
    page_number = request.GET.get('page', 1)  # Get the page number from query parameters
    jobs_page = paginator.get_page(page_number)

    title_query = request.GET.get('title', '').strip()
    location_query = request.GET.get('location', '').strip()

    if title_query:
        jobs = jobs.filter(title__icontains=title_query)

    if location_query:
        jobs = jobs.filter(location__icontains=location_query)

    context = {
        'jobs': jobs,
        'title_query': title_query,
        'location_query': location_query,
        'jobs_page': jobs_page
    }



    return render(request, "main/index.html", context=context)




def about(request):
    return render(request, "main/about.html")


