from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_album(request):
    if request.method == 'POST':
        album = forms.AlbumForm(request.POST)
        if album.is_valid():
            album.save()
            return redirect('addalbum')
    else:
        album = forms.AlbumForm()
    return render(request, 'add_album.html',{'form': album})
