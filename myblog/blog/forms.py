from django import forms
from .models import Article, comments, tempUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ArticlForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body' ]

class commentForm(forms.ModelForm):
    class Meta:
        model = comments
        fields = ['content']

class tempform(forms.ModelForm):
    qwertypass = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = tempUser
        fields = ['tempname', 'number', 'emailid', 'qwertypass']

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = []
