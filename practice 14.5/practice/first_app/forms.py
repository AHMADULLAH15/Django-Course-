# from django.forms import forms
from django import forms
from django.forms.widgets import NumberInput
from .models import MyModel

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100,label="Enter your Name")
    email = forms.EmailField(label='Enter your Email')
    message = forms.CharField(widget=forms.Textarea,label="Type your message")
    title = forms.CharField()
    description = forms.CharField() 
    password = forms.CharField(widget = forms.PasswordInput())
    agree = forms.BooleanField()
    date = forms.DateField()
    time = forms.TimeField()  # <--- This is the new field
    file = forms.FileField()  # <--- This is the new field
    comment = forms.CharField(widget=forms.Textarea)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    value = forms.DecimalField()


class MymodelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ('__all__')
        # fields = ('name', 'age','email')
        widgets ={
            'date_field': NumberInput(attrs={'type': 'date'})
        }