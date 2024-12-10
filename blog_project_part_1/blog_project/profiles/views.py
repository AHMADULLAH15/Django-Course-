from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_profiles(request):
    if request.method == "POST":
        add_profiles = forms.ProfilesForms(request.POST)
        if add_profiles.is_valid():
            add_profiles.save()
            return redirect('add_profiles')
    else:
        add_profiles = forms.ProfilesForms()
    return render(request, 'add_profiles.html',{'form' : add_profiles})