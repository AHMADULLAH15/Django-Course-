from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    # path('navigation/', include('navigation.urls')),
    # path('',views.home),
    path('about/',views.about),
    path('contact/',views.contact),
]