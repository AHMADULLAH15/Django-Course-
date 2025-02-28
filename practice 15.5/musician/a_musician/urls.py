from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.add_musician,name='add_musician'),
    path('',views.showMusician,name='homepage'),
    path('delete/<int:id>',views.delete,name='delete'),
    # path('edit/<int:id>',views.edit,name='edit'),
    path('edit/<int:id>',views.editAlbum,name='editalbum'),
    path('editMusician/<int:id>',views.editMusician,name='editmusician')
]
