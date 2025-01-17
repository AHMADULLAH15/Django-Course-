from django import forms
from .models import Catagory

class CatagoryForms(forms.ModelForm):
    class Meta:
        model = Catagory
        fields = ('__all__')