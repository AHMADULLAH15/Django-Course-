from django import forms
from .models import CategoryModel

class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ('category_name',)