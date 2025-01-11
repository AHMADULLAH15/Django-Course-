from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name='homepage'),
    path('form/',views.Exforms,name='form'),
    path('form/',views.testForm,name='testForm'),
    path('delete/<int:id>',views.MymodelData,name='deletedata'),
    path('ModelForm/',views.modelform,name='modelform'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
