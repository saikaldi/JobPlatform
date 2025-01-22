from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import UserLoginForm, UserRegistrationForm, ProfileForm
from .models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.urls import reverse
from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)

        if form.is_valid():
            user = form.save()
            print(f"User {user.username} successfully created.")
            auth.login(request, user)
            messages.success(request, f"{user.username}, you have successfully registered and logged into your account.")
            return redirect('main:index')
        else:
            print(form.errors)
            messages.error(request, "There was an error with your registration. Please check the form and try again.")
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Home - Registration',
        'form': form
    }
    return render(request, 'users/register.html', context)



def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)

        # Check if the form is valid
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Check if the user exists
            if not User.objects.filter(username=username).exists():
                messages.error(request, f"User '{username}' does not exist. Please register.")
                return redirect(reverse('users:register'))  # Adjust 'users:register' to your registration URL name

            # Authenticate the user
            user = auth.authenticate(username=username, password=password)
            remember_me = request.POST.get('remember_me')

            if user:
                auth.login(request, user)

                if remember_me:
                    # Extend the session duration to 30 days
                    request.session.set_expiry(30 * 24 * 60 * 60)  # 30 days
                else:
                    # End the session when the browser closes
                    request.session.set_expiry(0)

                messages.success(request, f'{username}, You successfully logged in')

                # Handle the 'next' parameter for redirection
                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('users:logout'):
                    return HttpResponseRedirect(redirect_page)

                return HttpResponseRedirect(reverse('main:index'))
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - Authentication',
        'form': form
    }
    return render(request, 'users/login.html', context)


@login_required
def logout(request):
    messages.success(request, f'{request.user.username}, You successfully logged out ')
    auth.logout(request)
    return redirect(reverse('main:index'))

@login_required
def profile(request):
    saved_jobs = request.user.saved_jobs.all()
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile successfully updated.')
            return redirect('users:profile')
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'Profile',
        'form': form,
        'user': request.user,  # Ensure user data is passed
        'saved_jobs': saved_jobs,
    }
    return render(request, 'users/profile.html', context)


