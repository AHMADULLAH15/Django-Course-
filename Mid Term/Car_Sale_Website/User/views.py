from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.views import LoginView,LogoutView
from . import forms
from django.contrib import messages
from django.views import View
from django.contrib.auth import logout
from car.models import Car,UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from car.models import UserProfile
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class UserCreation(CreateView):
    form_class = forms.UserRegistration
    template_name = 'registration.html'
    success_url = reverse_lazy('login')
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful')
            return redirect(self.success_url)
        return render(request,self.template_name,{'form' : form})
    
class Userlogin(LoginView):
    template_name = 'registration.html'
    success_url = reverse_lazy('homepage')
    def get_success_url(self):
        return reverse_lazy('homepage')
    def form_valid(self, form):
        messages.success(self.request,'Login Successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"Username or password incorrect")
        return super().form_invalid(form)
    

class UserLogout(View):
    # def get(self,request,*args, **kwargs):
    #     return redirect('login')
    def get(self,request,*args, **kwargs):
        logout(request)
        return redirect('login')
    
@method_decorator(login_required,name='dispatch')
class Updateuser(UpdateView):
    form_class = forms.UpdateUser
    template_name = 'registration.html'
    success_url = reverse_lazy('profile')
    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request,"Updated Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"There was an error updating your profile. Please try again.")
        return super().form_invalid(form)

   
def profile(request):
    user_profile = request.user.profile
    purchased_cars = user_profile.purchased_cars.all()
    return render(request,'profile.html', {'purchased_cars': purchased_cars})

def buy_now(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    # user_profile = request.user.profile
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if car.quantity > 0:
        car.quantity -= 1
        car.save()


        user_profile.purchased_cars.add(car)
        messages.success(request, f'You have successfully purchased {car.name}.')
    else:
        messages.error(request, 'Sorry, this car is out of stock.')

    return redirect('profile')  