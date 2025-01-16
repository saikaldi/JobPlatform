from django.shortcuts import render, redirect
from .forms import JobPostingForm
from django.contrib import messages

def posts(request):
    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Job posted successfully!")
            return redirect('jobs:jobs')
    else:
        form = JobPostingForm()
    return render(request, 'posts/posts.html', {'form': form})
