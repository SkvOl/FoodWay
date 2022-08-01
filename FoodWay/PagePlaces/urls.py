from django.urls import path, include
from . import views

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('add/', views.addPagePlaces, name = 'add_PagePlaces'),
    path('checkurl/', views.checkURL, name = 'checkurl'),
    path('all/', views.PagePlaceList.as_view(), name = 'showAllPagePlaces'), 
    path('delete/', views.deletePagePlace, name = 'deletePagePlace'),
    path('<str:slug>/edit/', views.editPagePlace, name = 'editPagePlace'),
    path('<str:slug>/', views.PagePlaceDetailView.as_view(), name = 'PagePlaces'),
]

