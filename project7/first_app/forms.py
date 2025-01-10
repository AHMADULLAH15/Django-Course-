from django import forms
from first_app.models import StudentModel
class StudentForms(forms.ModelForm):
    class Meta:
        model = StudentModel
        # fields = ('name', 'age', 'roll_number')
        fields = '__all__'
        # exclude = ['roll'] aita mani roll bade sob kicu show korbe
        labels = {
            'name': 'Your Name',
            'roll' : 'Your Roll',
            'father_name' : 'Your Father name',
            'address' : 'Your Address'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        help_texts ={
            'name' : 'Please enter your name',
            'roll' : 'Please enter your roll number',
        }
        error_messages = {
            'name' : {'required' : 'Please enter your name'},
            'roll' : {'required' : 'Please enter your roll number'},
            }
