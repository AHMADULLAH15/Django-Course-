from django.shortcuts import render
from datetime import datetime
# Create your views here.
def home(request):
    context = {
        'title': 'Home',
        'content': 'Welcome to the home page',
        'lst' : ['ahmad','ullah','i','love','only','mySelf'],
        'date': datetime.now(),
        'val': 'ahmad',
        'valName':
        [
    {'name': 'Josh', 'age': 19},
    {'name': 'Dave', 'age': 22},
    {'name': 'Joe', 'age': 31},
]

    }
    return render(request, 'home.html',context)