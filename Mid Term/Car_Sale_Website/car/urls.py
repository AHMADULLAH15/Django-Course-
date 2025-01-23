from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='homepage'),
    path('Brand/<slug:brand_slug>',views.home,name='BrandSlug'),
    path('ViewDetails/<int:id>/',views.DetailsView.as_view(),name = 'viewDetails')
]
