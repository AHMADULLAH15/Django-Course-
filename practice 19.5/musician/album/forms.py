from django import forms
from . import models
from django.forms.widgets import NumberInput

class AlbumForm(forms.ModelForm):
    class Meta:
        model = models.AlbumModel
        fields = '__all__'
        widgets = {
            'ReleaseDate' : NumberInput(attrs={'type': 'date'})
        }