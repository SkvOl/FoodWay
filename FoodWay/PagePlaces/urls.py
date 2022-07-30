from django.urls import path, include
from . import views

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('add/', views.addPagePlaces, name = 'add_PagePlaces'),
    path('<str:url>/', views.viewPagePlaces, name = 'PagePlaces')
]

