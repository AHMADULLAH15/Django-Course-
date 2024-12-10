from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def add_post(request):
    if request.method == 'POST':
        add_post = forms.PostForms(request.POST)
        if add_post.is_valid():
            add_post.save()
            return redirect('homepage')
    else:
        add_post = forms.PostForms()
    return render(request,'add_post.html',{'form' : add_post})


def edit_post(request,id):
    post = models.Post.objects.get(pk = id)
    post_forms = forms.PostForms(instance=post)
    if request.method == 'POST':
        post_forms = forms.PostForms(request.POST,instance=post)
        if post_forms.is_valid():
            post_forms.save()
            return redirect('homepage')
    return render(request,'add_post.html',{'form' : post_forms})

def delete_post(request,id):
    post = models.Post.objects.get(pk = id)
    post.delete()
    return redirect('homepage')