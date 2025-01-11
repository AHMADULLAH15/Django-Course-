from django.shortcuts import render,redirect
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, render, redirect
from . import forms
from . import models
from album import models as albumModel
from album.models import AlbumModel
from album.forms import AlbumForm
from .models import MusicianModel

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
            return redirect("add_musician")
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