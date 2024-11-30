from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name = 'about'),
    path('form/',views.form,name='form'),
    # path('forms/',views.djForm, name = 'djForms')
    # path('forms/',views.StudentForm, name = 'djForms')
    path('forms/',views.PasswordValidation, name = 'djForms')
]
