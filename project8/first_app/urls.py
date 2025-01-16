from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('user_login/',views.user_login,name='login'),
    path('user_logout/',views.user_logout,name='logout'),
    path('passChange/',views.passChange,name='passChange'),
    path('passChange2/',views.passChange2,name='passChange2'),
    path('profile/',views.profile,name='profile'),
    # path('changeUserDate/',views.ChangeUserData,name='ChangeUserData'),
]
