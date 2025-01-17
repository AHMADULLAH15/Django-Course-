from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name= 'homepage'),
    path('userCreationForm/',views.userCreation,name= 'usercreation'),
    path('userLogin/',views.userLogin,name= 'userLogin'),
    path('userLogout/',views.userLogout,name= 'userLogout'),
    path('profile/',views.profilePage,name= 'profile'),
    path('passwordChange/',views.userPassChange,name= 'passChange'),
    path('userPassChangeWithourOld/',views.userPassChangeWithourOld,name= 'passChangeold'),
]
