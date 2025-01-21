from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.MusicianModel
        fields = '__all__'

class UserRegistration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']