from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class BlogUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        model = Users
        fields = ('username',)

class BlogAuthenticationForm(AuthenticationForm):

    class Meta(AuthenticationForm):
        model = Users
        fields = ('username',)