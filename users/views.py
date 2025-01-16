from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm, ProfileForm
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from django.contrib import auth, messages

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user=form.save()
            print(f"User {user.username} successfully created.")

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                messages.success(request, f"{user.username}, You have successfully registered and logged into your account")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Home - Registration',
        'form': form
    }
    return render(request, 'users/register.html', context)


def login_view(request):  # Avoid using "Login" as the function name
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Logs in the user
            messages.success(request, f'Welcome {username}!')
            return redirect('index')  # Redirects to the "index" view
        else:
            messages.error(request, 'Account does not exist. Please sign up.')

    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def logout(request):
    messages.success(request, f'{request.user.username}, You successfully logged out ')
    auth.logout(request)
    return redirect(reverse('main:index'))

# @login_required
def profile(request):
    # if request.method == 'POST':
    #     form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, f' Profile successfully updated')
    #         return HttpResponseRedirect(reverse('user:profile'))
    # else:
    #     form = ProfileForm(instance=request.user)
    # context = {
    #     'title': 'Home - Cabinet',
    #     'form': form,
    # }
    return render(request, 'users/profile.html')
