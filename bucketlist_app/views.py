from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import LoginForm, SignUpForm


# Create your views here.
def index(request):
    """Root route for the application."""
    loginForm = LoginForm()
    signupForm = SignUpForm()
    if (request.method == "POST"):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                print('Get out of here!!!')
    return render(request, 'index.html', {"loginForm": loginForm, "signupForm": signupForm})


def dashboard(request):
    user = request.user
    return render(request, 'dashboard.html', {'user': user})
