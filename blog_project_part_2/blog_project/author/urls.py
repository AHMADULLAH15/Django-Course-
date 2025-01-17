from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit',views.editprofile,name='editprofile'),
    path('profile/edit/passwordChange/',views.passChange,name='passwordchange'),
]
