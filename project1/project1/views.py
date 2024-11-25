from django.http import HttpResponse

def home(response):
    return HttpResponse("Hello, world!")

def contact(response):
    return HttpResponse("Contact us at support@myapp.com")