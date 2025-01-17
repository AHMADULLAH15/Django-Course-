from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_categories(request):
    if request.method == 'POST':
        add_categories = forms.CatagoryForms(request.POST)
        if add_categories.is_valid():
            add_categories.save()
            return redirect('add_categories')
    else:
        add_categories = forms.CatagoryForms()
    return render(request,'add_categories.html',{'form' : add_categories})