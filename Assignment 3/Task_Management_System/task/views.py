from django.shortcuts import render,redirect
from . import forms
from .models import TaskModel
# Create your views here.
def add_task(request):
    if request.method == 'POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_task')
    else:
        form = forms.TaskForm()
    return render(request, 'add_task.html',{'form' : form})

def show_task(request):
    task = TaskModel.objects.prefetch_related('categories')
    return render(request, 'show_task.html',{'task' : task})

def delete(request,id):
    task = TaskModel.objects.get(pk = id).delete()
    return redirect('show_task')

def edit(request,id):
    task = TaskModel.objects.get(pk = id)
    if request.method == 'POST':
        form = forms.TaskForm(request.POST,instance = task)
        if form.is_valid():
            form.save()
            return redirect('show_task')
    else:
        form = forms.TaskForm(instance = task)
    return render(request, 'add_task.html',{'form' : form})
