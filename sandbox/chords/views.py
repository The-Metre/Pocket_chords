from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.db import IntegrityError
from .models import *

def index(request):

    if request.user.is_authenticated:
        return render(request, 'chords/main_page.html')
    else:
        return HttpResponseRedirect(reverse('login'))

def login_view(request):
    if request.method == 'POST':

        # Attempt to sign user in
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'chords/login.html', {
                'message': 'Invalid email and/or password.'
            })
    else:
        return render(request, 'chords/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        # Check that passwords matches
        password = request.POST['password']
        confirm_password = request.POST['confirmation']
        if password != confirm_password:
            return render(request, 'chords/register.html', {
                'message': 'Passwords must match.'
            })

        # Attempt to create new user
        try:
            user = CustomUser.objects.create_user(username, password)
            user.save()
        except IntegrityError:
            return render(request, 'chords/register.html', {
                'message': 'Username already taken.'
            })
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'chords/register.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
