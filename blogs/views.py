from django.shortcuts import render, redirect
from datetime import datetime
import re
from .models import *
from django.contrib.auth import authenticate, login as auth_login, logout as lgout
from .forms import *
from django.contrib.auth.hashers import Argon2PasswordHasher
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    articles = Articles.objects.all().values()
    
    for i in range(len(articles)):
        username = Users.objects.filter(id=articles[i]['userid']).values('username')
        articles[i]['username'] = username[0]['username']
    
    data = {"content": [articles]}
    
    return render(request, 'index.html', context=data)

def article(request, id):
    articles = Articles.objects.filter(id=id).values()
    
    for i in range(len(articles)):
        username = Users.objects.filter(id=articles[i]['userid']).values('username')
        articles[i]['username'] = username[0]['username']
    
    data = {"content": [articles]}
    
    return render(request, 'article.html', context=data)

def signup(request):

    if request.user.is_authenticated:
        return redirect('/user/profile')

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
    if request.user.is_authenticated:
        return redirect('/user/profile')
    
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

@login_required
def profile(request):
    user = request.user
    user_data = Users.objects.filter(id=user.id).values()
    user_articles = Articles.objects.filter(userid=user.id).values()
    
    for i in range(len(user_articles)):
        user_articles[i]['username'] = user
    
    return render(request, 'profile.html', context={'articles': [user_articles]})

@login_required
def logout(request):
    lgout(request)
    return redirect('/')

@login_required
def settings(request):
    user = request.user

    data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
    }
    
    if request.method == "POST":
        
        cur_user = Users.objects.get(username=request.user.username)
        form = BlogUserProfileForm(data=request.POST, instance=cur_user)

        if form.is_valid():

            form.save()
        
            return redirect('/user/settings')

        return render(request, 'settings.html', context={'form': form})

    form = BlogUserProfileForm(data=data)
    return render(request, 'settings.html', context={'form': form})

def other_profile(request, username):
    if username == request.user.username:
        return redirect('/user/profile')
    
    user_data = Users.objects.filter(username=username).values()[0]
    
    user_articles = Articles.objects.filter(userid=user_data['id']).values()
    
    for i in range(len(user_articles)):
        user_articles[i]['username'] = user_data['username']

    return render(request, 'other_profile.html', context={'articles': [user_articles], 'userdata': user_data})

@login_required
def change_password(request):
    if request.method == "POST":

        form = BlogUserChangePassword(user=request.user, data=request.POST)
        
        if form.is_valid():
            
            form.save()
        
            return redirect('/user/login')
            

        return render(request, 'change-password.html', context={'form': form})

    form = BlogUserChangePassword(user=request.user)
    return render(request, 'change-password.html', context={'form': form})

@login_required
def articles_new(request):
    if request.method == "POST":
        form = ArticlesCreationForm(data=request.POST)

        if form.is_valid():

            uid = request.user.id
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            
            article = Articles.objects.create(userid=uid, title=title, text=text)

            if article.id:
                return redirect('/user/profile')

        return render(request, 'new_article.html', context={'form': form})

    form = ArticlesCreationForm()
    return render(request, 'new_article.html', context={'form': form})