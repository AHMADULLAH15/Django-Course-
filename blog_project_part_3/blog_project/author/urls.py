from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/',views.register,name='register'),
    # path('login/',views.user_login,name='login'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    # path('logout/',views.user_logout,name='logout'),
    path('logout/',views.UserLogoutView.as_view(),name='logout'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit/',views.editprofile,name='editprofile'),
    path('profile/edit/passwordChange/',views.passChange,name='passwordchange'),
]
