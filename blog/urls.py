"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import blogs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('article/<int:id>', blogs.views.article),
    path('', blogs.views.index),
    path('user/signup', blogs.views.signup),
    path('user/login', blogs.views.login),
    path('user/profile', blogs.views.profile),
    path('user/logout', blogs.views.logout),
    path('user/settings', blogs.views.settings),
    path('user/change-password', blogs.views.change_password),
    path('user/profile/<str:username>', blogs.views.other_profile),
    path('acticles/new', blogs.views.articles_new)
]
