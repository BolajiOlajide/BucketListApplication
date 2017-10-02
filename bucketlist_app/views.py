from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, SignUpForm, BucketListForm
from .models import Bucketlist, Items


# Create your views here.
def index(request):
    """Root route for the application."""
    loginForm = LoginForm()
    signupForm = SignUpForm()
    if (request.method == "POST"):
        if 'first_name' in request.POST:
            form = SignUpForm(request.POST)
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            password2 = request.POST.get('password2', None)
            email = request.POST.get('email_address', None)
            first_name = request.POST.get('first_name', None)
            last_name = request.POST.get('last_name', None)
            if (password == password2) and form.is_valid():
                user, created = User.objects.get_or_create(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name
                )
                if created:
                    user.set_password(password)
                    user.save()
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')                           
        else:
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


@login_required
def dashboard(request):
    user = request.user
    bucketlists = Bucketlist.objects.filter(user=user)
    bucketlist_form = BucketListForm()
    if (request.method == "POST"):
        form = BucketListForm(request.POST)
        if form.is_valid():
            _bucketlist, created = Bucketlist.objects.get_or_create(
                name=request.POST.get('name'),
                user=user
            )
            if created:
                _bucketlist.save()
            return redirect('dashboard')
    return render(request, 'dashboard.html', {
        'user': user,
        'bucketlists': bucketlists,
        'bucketlist_form': bucketlist_form
    })


@login_required
def logout_view(request):
    logout(request)
    return redirect('homepage')
