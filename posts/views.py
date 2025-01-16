from django.shortcuts import render, redirect
from .forms import JobPostingForm

def posts(request):
    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = JobPostingForm()
    return render(request, 'posts/posts.html', {'form': form})
