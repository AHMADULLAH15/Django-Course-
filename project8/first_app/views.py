from django.shortcuts import render,redirect
from .forms import RegisterForm,ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash #ai gula django teke build in vabe dewa teke login logut er jonno 
# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request,"User Account Created Successfully")
                form.save()
                print(form.cleaned_data)
        else:
            form = RegisterForm()  
        return render(request,'signup.html',{'form' : form})
    else:
        return redirect('profile')

# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request=request, data=request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['username']
#             userpassword = form.cleaned_data['password']
#             user = authenticate(username=name, password=userpassword)
#             if user is not None:
#                 login(request, user)
#                 return redirect('profile')
#             else:
#                 messages.error(request, "Invalid username or password.")  # Error for failed authentication
#         else:
#             messages.error(request, "Invalid username or password.")  # Error for invalid form

#     # If GET request or POST fails, show login form
#     form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpassword = form.cleaned_data['password']
                user = authenticate(username=name, password=userpassword)
                if user is not None:
                    login(request, user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('profile')


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ChangeUserData

def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, "User account updated successfully!")
                form.save()
                return redirect('profile')  # Redirect to the same page after saving
        else:
            form = ChangeUserData( instance=request.user)  # Pre-fill with user data
        return render(request, 'profile.html', {'form': form})
    else:
        return redirect('signup')  # Redirect to signup if user is not authenticated


def user_logout(request):
    logout(request)
    # messages.success(request, "You have been logged out successfully.")
    return redirect('login')

def passChange(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user = request.user,data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user = request.user)
        return render(request,'passChange.html',{'form':form})
    else:
        return redirect('login')

def passChange2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user = request.user,data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user = request.user)
        return render(request,'passChange.html',{'form':form})
    else:
        return redirect('login')

def update_user_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST,instance = request.user)
            if form.is_valid():
                messages.success(request,"User Account update Successfully")
                form.save()
                print(form.cleaned_data)
        else:
            form = ChangeUserData()  
        return render(request,'profile.html',{'form' : form})
    else:
        return redirect('singup')
    
