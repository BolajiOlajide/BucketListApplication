from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import LoginForm, SignUpForm


# Create your views here.
def index(request):
    """Root route for the application."""
    loginForm = LoginForm()
    signupForm = SignUpForm()
    if (request.method == "POST"):
        if 'first_name' in request.POST:
            print('signing up!')
            form = SignUpForm(request.POST)
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            password2 = request.POST.get('password2', None)
            email = request.POST.get('email_address', None)
            if username and password and email and (password == password2):
                user, created = User.objects.get_or_create(username=username, email=email)
                if created:
                    user.set_password(password)
                    user.save()
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')                           
        else:
            print('logging in')
            form = LoginForm(request.POST)
            if form.is_valid():
                username = request.POST.get('username', None)
                password = request.POST.get('password', None)
                if username and password:
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect('dashboard')
                    else:
                        return redirect('homepage')
    return render(request, 'index.html', {"loginForm": loginForm, "signupForm": signupForm})


def dashboard(request):
    user = request.user
    return render(request, 'dashboard.html', {'user': user})
