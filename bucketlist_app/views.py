from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, SignUpForm, BucketListForm, ItemForm
from .helper import get_or_none
from .models import Bucketlist, Items
from .pusher import pusher_client


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
                        pusher_client.trigger('my-channel', 'my-event', {
                            'message': 'Invalid login credentials!'
                        })
    return render(request, 'index.html', {
        "loginForm": loginForm,
        "signupForm": signupForm
    })


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
    pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})
    count = len(bucketlists)
    return render(request, 'dashboard.html', {
        'user': user,
        'bucketlists': bucketlists,
        'bucketlist_form': bucketlist_form,
        'count': count
    })


@login_required
def logout_view(request):
    logout(request)
    return redirect('homepage')


@login_required
def delete_bucketlist(request, bucketlist_id):
    _bucketlist = Bucketlist.objects.get(pk=bucketlist_id)
    _name = _bucketlist.name
    if _bucketlist:
        _bucketlist.delete()
    pusher_client.trigger('my-channel', 'my-event', {
        'message': 'Bucketlist {} successfully deleted'.format(_name)
    })
    return redirect('dashboard')


@login_required
def bucketlist_details(request, bucketlist_id):
    _bucketlist = get_or_none(Bucketlist, pk=bucketlist_id)
    if _bucketlist:
        _items = Items.objects.filter(bucketlist=_bucketlist)
        item_form = ItemForm()
        if (request.method == 'POST'):
            print('kay')
            form = ItemForm(request.POST)
            _done = True if request.POST.get('done') else False
            # import pdb;pdb.set_trace()
            if form.is_valid():
                _item, created = Items.objects.get_or_create(
                    name=request.POST.get('name'),
                    done=_done,
                    bucketlist=_bucketlist
                )
            if created:
                _item.save()
            return redirect('details', bucketlist_id=_bucketlist.id)
        return render(request, 'details.html', {
            'bucketlist': _bucketlist,
            'items': _items,
            'item_form': item_form
        })
    return redirect('dashboard')
