from django.shortcuts import render,redirect
from . import forms
from .forms import ExampleForm,MymodelForm
from . import models
# Create your views here.
def home(request):
    MyModel = models.MyModel.objects.all()
    return render(request, 'home.html',{'data' : MyModel})

from django.contrib import messages

def modelform(request):
    if request.method == 'POST':
        form = MymodelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Data submitted successfully!")
            return redirect('modelform')
    else:
        form = MymodelForm()
    return render(request, 'Model_Form.html', {'form': form})


def MymodelData(request,id):
    MyModel = models.MyModel.objects.get(pk = id).delete()
    return redirect("homepage")

def Exforms(request):
    if request.method == 'POST':
        form = forms.ExampleForm(request.POST,request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # message = form.cleaned_data['message']
            # print(f"Received message from {name} ({email} : {message}")
            # return render(request,'SuccessPage.html',{'name':name ,'email':email ,'message':message})
            print(form.cleaned_data)
            file = form.cleaned_data['file']
            with open('./first_app/upload/' + file.name,'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            return render(request, 'SuccessPage.html', {'form': form}) 
    else:
        form = ExampleForm()
    return render(request, 'SuccessPage.html', {'form': form})  
        

def testForm(request):
    if request.method == 'POST':
        name = request.POST.get("username")
        email = request.POST.get("email")
        return render(request, 'form.html',{'name' : name ,'email' : email})
    return render(request, 'form.html')

def success(request):
    return render(request,"SuccessPage.html")