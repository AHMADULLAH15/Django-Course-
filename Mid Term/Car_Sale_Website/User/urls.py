from django.urls import path
from . import views
urlpatterns = [
    path('Registration/', views.UserCreation.as_view(),name = 'usercreation'),
    path('login/', views.Userlogin.as_view(),name = 'login'),
    path('logout/', views.UserLogout.as_view(),name = 'logout'),
    path('updateProfile/', views.Updateuser.as_view(),name = 'Updateuser'),
    path('profile/',views.profile,name='profile'),
    path('buy-now/<int:car_id>/', views.buy_now, name='buy_now'),
]
