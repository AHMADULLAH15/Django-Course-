from django.shortcuts import render
from . forms import contactForm,StudentData,PasswordValidationProject
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    print(request.POST)
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        select = request.POST.get('select')
        # password = request.POST.get('userpassword')
        # print(name, email, password)
        return render(request, 'about.html',{'name' : name,'email':email,'select':select})
    else:
        return render(request, 'about.html')

def form(request):
    return render(request, 'form.html')

def djForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST,request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            # wb+ use korteci file ta binary ba onno kono format a asleo accept korte pare moto
            # chunk use korteci file er Gb jodi 1 gb take besi hoy aita handle korte pare moto
            with open('./first_app/upload/' + file.name,'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
            return render(request,'djForms.html',{'form' : form})
    else:
        form = contactForm()
    return render(request,'djForms.html',{'form' : form})


def StudentForm(request):
    if request.method == 'POST':
        form = StudentData(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentData()
    return render(request,'djForms.html',{'form' : form})

def PasswordValidation(request):
    if request.method == 'POST':
        form = PasswordValidationProject(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PasswordValidationProject()
    return render(request,'djForms.html',{'form' : form})