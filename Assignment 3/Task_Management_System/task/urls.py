from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_task,name='show_task'),
    path('add/',views.add_task,name='add_task'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
]
