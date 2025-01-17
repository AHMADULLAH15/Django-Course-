from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,update_session_auth_hash,authenticate
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def home(request):
    return render(request, 'home.html')

def userCreation(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            userForm = forms.UserRegistrationForm(request.POST)
            if userForm.is_valid():
                messages.success(request,"Account Created Successfully")
                userForm.save()
                return redirect('homepage')
        else:
            userForm = forms.UserRegistrationForm()
        return render(request, 'userCreationForm.html', {'form': userForm,'type' : 'Registration'})
    else:
        return redirect('profile')


def userLogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            loginForm = AuthenticationForm(request.POST,data = request.POST)
            if loginForm.is_valid():
                user = loginForm.cleaned_data['username']
                password = loginForm.cleaned_data['password']
                user = authenticate(username=user, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request,"Logged In Successfully")
                    return redirect('profile')
                else:
                    messages.error(request, "Invalid Username or Password")
            return render(request,'userCreationForm.html',{'form' : loginForm,"type" : 'Login'})
        else:
            loginForm = AuthenticationForm()
            return render(request, 'userCreationForm.html',{'form' : loginForm,"type" :"Login"})
    else:
        return redirect('profile')

@login_required
def profilePage(request):
    return render(request, 'profile.html')

def userLogout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully")
        return redirect('homepage')
    

def userPassChange(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            passChangeForm = PasswordChangeForm(request.user, request.POST)
            if passChangeForm.is_valid():
                user = passChangeForm.save()
                update_session_auth_hash(request, user)
                messages.success(request,"Password Changed Successfully")
                return redirect('profile')
            else:
                messages.error(request,"Invalid Password")
            return render(request,'userCreationForm.html',{'form' : passChangeForm,'type' : 'Password Change'})
        else:
            passChangeForm = PasswordChangeForm(request.user)
            return render(request,'userCreationForm.html',{'form' : passChangeForm,'type' : 'Password'})
    else:
        return redirect('userLogin')

    
def userPassChangeWithourOld(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            passChange = SetPasswordForm(user = request.user, data = request.POST)
            if passChange.is_valid():
                user = passChange.save()
                update_session_auth_hash(request, user)
                messages.success(request,"Password Changed Successfully")
                return redirect('profile')
        else:
            passChange = SetPasswordForm(request.user)
            return render(request,'userCreationForm.html',{'form' : passChange,'type' : 'Password Change'})
    else:
        return redirect('userLogin')