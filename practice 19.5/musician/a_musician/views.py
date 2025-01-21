from django.shortcuts import render,redirect
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, render, redirect
from . import forms
from . import models
from album import models as albumModel
from album.models import AlbumModel
from album.forms import AlbumForm
from .models import MusicianModel
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View
from django.contrib.auth import logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.conf import settings
# Create your views here.
def add_musician(request):
    # akta inline formset create korteci AlbumModel related to MusicianModel
    AlbumFormSet = inlineformset_factory(MusicianModel,AlbumModel,form=AlbumForm,extra=1,can_delete=False)
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)
        albumForm = AlbumFormSet(request.POST)
        if form.is_valid() and albumForm.is_valid():
            musician = form.save() # save musician form
            albumForm.instance = musician #link album to the musician
            albumForm.save() # save album form
            return redirect("add_musician")
    else:
        form = forms.MusicianForm()
        albumForm = AlbumFormSet()
    return render(request,'add_musician.html',{'form': form ,'album' : albumForm})

def showMusician(request):
    musicians = models.MusicianModel.objects.all()
    # albums = albumModel.AlbumModel.objects.all()
    albums = models.MusicianModel.objects.prefetch_related('albums')
    return render(request,'home.html',{'musicians':musicians ,'albums' : albums})

def edit(request, id):
    # Retrieve the musician object or return 404 if not found
    musician = get_object_or_404(models.MusicianModel, id=id)
    
    # Create an inline formset for AlbumModel
    AlbumFormSet = inlineformset_factory(
        models.MusicianModel,
        AlbumModel,
        form=AlbumForm,
        extra=0,
        can_delete=False
    )
    
    if request.method == 'POST':
        # Initialize the musician and album forms with POST data
        form = forms.MusicianForm(request.POST, instance=musician)
        albumForm = AlbumFormSet(request.POST, instance=musician)
        if form.is_valid() and albumForm.is_valid():
            form.save()  # Save musician
            albumForm.save()  # Save album formset
            return redirect("homepage")
    else:
        # Initialize the forms with existing data for GET requests
        form = forms.MusicianForm(instance=musician)
        albumForm = AlbumFormSet(instance=musician)
    
    return render(request, 'add_musician.html', {'form': form, 'album': albumForm})

def delete(request,id):
    musician = models.MusicianModel.objects.get(id=id).delete()
    return redirect('homepage')

def editMusician(request,id):
    musician = get_object_or_404(models.MusicianModel, id=id)
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST,instance=musician)
        if form.is_valid():
            form.save()
            return redirect('add_musician')
    else:
        form = forms.MusicianForm(instance=musician)
    return render(request,'add_musician.html',{'form':form})

def editAlbum(request,id):
    album = get_object_or_404(AlbumModel,id=id)
    if request.method == 'POST':
        form = AlbumForm(request.POST,instance=album)
        if form.is_valid():
            form.save()
            return redirect('add_musician')
    else:
        form = AlbumForm(instance=album)
    return render(request,'add_musician.html',{'form':form})

class UserRegister(CreateView):
    form_class = forms.UserRegistration
    template_name = 'registration.html'
    success_url = reverse_lazy('homepage')
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})
    
class UserLogin(LoginView):
    template_name = 'registration.html'
    success_url = reverse_lazy('homepage')
    def get_success_url(self):
        return reverse_lazy('homepage')
    def form_valid(self, form):
        messages.success(self.request,"Logged in Successfully")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,'Logged in information incorrect')
        return super().form_invalid(form)

@method_decorator(login_required,name='dispatch')
class UserLogout(View):
    # def get(self, request, *args, **kwargs):
    #     logout(request)
    #     return redirect('login')
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)
    