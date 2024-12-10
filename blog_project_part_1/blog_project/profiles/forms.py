from django import forms
from .models import Profiles

class ProfilesForms(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ('__all__')