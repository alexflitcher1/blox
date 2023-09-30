from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin 
from .forms import AuthenticationForm

# Register your models here.
admin.site.register(Articles)
admin.site.register(Users, UserAdmin)