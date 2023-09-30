from django.shortcuts import render, redirect
from datetime import datetime
import re
from .models import *
from django.contrib.auth import authenticate, login as auth_login
from .forms import *
from django.contrib.auth.hashers import Argon2PasswordHasher
from django.http import HttpResponse


# Create your views here.
def index(request):
    data = {"content": [Articles.objects.all().values()]}
    return render(request, 'index.html', context=data)

def article(request, id):
    data = {"content": [Articles.objects.filter(id=id).values()]}
    return render(request, 'article.html', context=data)

def signup(request):
    if request.method == "POST":
        form = BlogUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('/')
        return render(request, 'signup.html', context={'form': form})
    form = BlogUserCreationForm()
    return render(request, 'signup.html', context={'form': form})

def login(request):
    if request.method == "POST":
        form = BlogAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('/')
        return render(request, 'login.html', context={'form': form})
    form = BlogAuthenticationForm()
    return render(request, 'login.html', context={'form': form})