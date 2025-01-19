from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from post.models import Post
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.views import View
# Create your views here.
# def add_author(request):
#     if request.method == 'POST':
#         author_form = forms.AuthorForms(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect('add_author')
#     else:
#         author_form = forms.AuthorForms()
#     return render(request,'add_author.html',{'form' : author_form})

def register(request):
    if request.method == 'POST':
        registerForm = forms.RegisterForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            messages.success(request,"Account created Successfully")
            return redirect('register')
    else:
        registerForm = forms.RegisterForm()
    return render(request,'register.html',{'form' : registerForm,'type' : 'Register'})

# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request=request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, "Login successful")
#                 return redirect('profile')  # Redirect to the desired URL after login
#             else:
#                 messages.error(request, "Invalid username or password")
#         # If form is not valid, re-render the login form with error messages
#         return render(request, 'register.html', {'form': form, 'type': 'Login'})
#     else:
#         form = AuthenticationForm()
#         return render(request, 'register.html', {'form': form, 'type': 'Login'})

class UserLoginView(LoginView):
    template_name = 'register.html'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request,"Logged in successfully")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.ERROR(self.request,"Logged in information incorrect")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'type': 'login'})
        return context
    
    
@login_required
def profile(request):
    data = Post.objects.filter(author=request.user)
    # data = Post.objects.all()
    return render(request,'profile.html',{'data' : data})


@login_required
def editprofile(request):
    if request.method == 'POST':
        profileForm = forms.UserDataChange(request.POST,instance = request.user)
        if profileForm.is_valid():
            profileForm.save()
            messages.success(request,"Account update Successfully")
            return redirect('profile')
    else:
        profileForm = forms.UserDataChange(instance = request.user)
    return render(request,'updateProfile.html',{'form' : profileForm,'type' : 'profile'})


def passChange(request):
    if request.method == 'POST':
        Form = PasswordChangeForm(request.user,data = request.POST)
        if Form.is_valid():
            Form.save()
            messages.success(request," Password Change Successfully")
            update_session_auth_hash(request,Form.user)
            return redirect('profile')
    else:
        Form = PasswordChangeForm(user=request.user)
    return render(request,'passChange.html',{'form' : Form,'type' : 'Password Change'})


# def user_logout(request):
#     logout(request)
#     return redirect('login')
# class UserLogoutView(LogoutView):
#     template_name = 'register.html'  # Ensure the correct template file name

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context.update({'type': 'Logout'})
#         return context
class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')