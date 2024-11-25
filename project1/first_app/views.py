from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def course(response):
    return HttpResponse("This is a course page")

def about(response):
    return HttpResponse("This is an about page")

def home(response):
    return HttpResponse("This is a first app home page")