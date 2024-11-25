from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    age = 21
    d = {'author' : 'AHMAD', 'age': 21,
        'is_adult': age >= 21,'is_teenager': 10 <= age <= 19,
        'courses' :[
            {'id':1,'name': 'Python', 'price': 100},
            {'id':2,'name': 'Java', 'price': 200},
            {'id':3,'name': 'C++', 'price': 300}

        ],
        'lst': ['i','love','python'],
        'birthday' : datetime.datetime.now()}
    return render(request, 'home.html',d)
