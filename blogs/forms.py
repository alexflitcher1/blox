from .models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm

class BlogUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        model = Users
        fields = ('username',)

class BlogAuthenticationForm(AuthenticationForm):

    class Meta(AuthenticationForm):
        model = Users
        fields = ('username',)

class BlogUserProfileForm(ModelForm):

    class Meta(ModelForm):
        model = Users
        fields = ('first_name', 'last_name', 'email')

class BlogUserChangePassword(PasswordChangeForm):

    class Meta(PasswordChangeForm):
        model = Users
        fields = ('password',)

class ArticlesCreationForm(forms.Form):
    title = forms.CharField(max_length=254)
    text = forms.CharField(widget=forms.Textarea(attrs={"rows":"15"}))

    class Meta(forms.Form):
        model = Articles
        fields = ('title', 'text')

    def clean(self):
        title = self.cleaned_data.get('title')
        text = self.cleaned_data.get('text')

        if not title:
            self.add_error("title", 'Incorrect title')
        
        if len(text.replace(' ', '')) < 500:
            self.add_error(
                "text", 
                'Length of text without spaces \
                must be more than 500 symbols'
            )

        return self.cleaned_data