from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404, redirect
from .models import JobPosting
from .forms import JobApplicationForm
from django.contrib import messages

# Create your views here.


def jobs(request):
    jobs = JobPosting.objects.all()
    return render(request, "jobs/job_find.html", {'jobs':jobs})

def job_detail(request, pk):
    job = get_object_or_404(JobPosting, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})


@login_required
def apply_for_job(request, pk):
    if not request.user.is_authenticated:
        messages.warning(request, "Please log in or register to apply for jobs.")
        return redirect(request.META.get('HTTP_REFERER', 'jobs:jobs'))  # Redirect back to the same page

    job = get_object_or_404(JobPosting, pk=pk)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job  # Link the application to the job
            application.save()
            messages.success(request, "Application submitted successfully!")

            return redirect('jobs:job_detail', pk=job.pk)
    else:
        form = JobApplicationForm()

    return render(request, 'jobs/apply_form.html', {'form': form, 'job': job})


@login_required
def save_job(request, job_id):
    if not request.user.is_authenticated:
        messages.warning(request, "Please log in or register to save jobs.")
        return redirect(request.META.get('HTTP_REFERER', 'users:register'))  # Redirect back to the same page

    job = get_object_or_404(JobPosting, id=job_id)
    if job.saved_by.filter(id=request.user.id).exists():
        job.saved_by.remove(request.user)  # Unsave if already saved
        messages.info(request, "Job removed from your saved list.")
    else:
        job.saved_by.add(request.user)  # Save the job
        messages.success(request, "Job added to your saved list.")
    return redirect(request.META.get('HTTP_REFERER', 'main:index'))


def search_results(request):
    # Get search parameters
    title_query = request.GET.get('title', '').strip()
    location_query = request.GET.get('location', '').strip()

    # Filter jobs based on the search criteria
    jobs = JobPosting.objects.all()

    if title_query:
        jobs = jobs.filter(title__icontains=title_query)

    if location_query:
        jobs = jobs.filter(location__icontains=location_query)

    context = {
        'jobs': jobs,
        'title_query': title_query,
        'location_query': location_query,
    }
    return render(request, 'jobs/job_search_results.html', context)