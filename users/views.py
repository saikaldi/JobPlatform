from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm, ProfileForm
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm, ProfileForm

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
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            remember_me = request.POST.get('remember_me')

            messages.get_messages(request)

            if user:
                auth.login(request, user)
                if remember_me:
                    # Extend the session duration to 30 days
                    request.session.set_expiry(30 * 24 * 60 * 60)  # 30 days
                else:
                    # End the session when the browser closes
                    request.session.set_expiry(0)

                messages.success(request, f'{username}, You successfully logged in')

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))

                return HttpResponseRedirect(reverse('main:index'))
        else:
            # Add error message for invalid credentials
            messages.error(request, 'Invalid username or password. Please try again.')


    else:

        form = UserLoginForm()

    context = {
        'title': 'Home - Authentication',
        'form':form
    }
    return render(request, 'users/login.html', context)

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
