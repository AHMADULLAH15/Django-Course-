from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(max_length=100, label='userName',help_text='Total length must be within 70 characters', required=False,widget=forms.Textarea(attrs={'id': 'text_area','class': 'classAhmad','placeholder':"Enter your name"}))
    file = forms.FileField()
    email = forms.EmailField()
    # age = forms.IntegerField()
    age = forms.CharField(widget=forms.NumberInput)
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    Birthday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    Appoirtment = forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    choice = [('S', 'Small'),('M','Medium'),('L', 'Large')]
    size = forms.ChoiceField(choices=choice, label='Size',widget=forms.RadioSelect)
    MEALS = [('P','peparoni'),('M','Mashroom'),('B','Beef')]
    Pizza = forms.MultipleChoiceField(choices=MEALS,label='Pizza',widget=forms.CheckboxSelectMultiple)
    message = forms.CharField(widget=forms.Textarea)

# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError('Name must be at least 10 characters')
    #     return valname
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     # if '@' not in valemail:
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('Email must contain @')
    #     return valemail
    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname) < 10:
    #         raise forms.ValidationError('Name must be at least 10 characters')
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('Email must contain .com')
        # return cleaned_data
def lenCheck(value):
    if len(value) < 10:
        raise forms.ValidationError('Name must be at least 10 characters')
class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput,validators=[validators.MinLengthValidator(10,message='Name must be at least 10 characters')])
    text = forms.ChoiceField(widget=forms.TextInput,validators=[lenCheck])
    email = forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message='Enter a valid email')])
    age = forms.IntegerField(required=False,validators=[validators.MaxValueValidator(50,message='max age 50'),validators.MinValueValidator(10,message='min age 10')])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png','jpg'],message='File must be pdf')])


class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valPass = self.cleaned_data['password']
        valConfirmPass = self.cleaned_data['confirm_password']
        valName = self.cleaned_data['name']
        if valPass != valConfirmPass:
            raise forms.ValidationError('Password and confirm password must be same')
        if len(valName) < 10:
            raise forms.ValidationError('Name must be at least 10 characters')