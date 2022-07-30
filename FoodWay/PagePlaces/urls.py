from django.urls import path, include
from . import views

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('add/', views.addPagePlaces, name = 'add_PagePlaces'),
    path('checkurl/', views.checkURL, name = 'checkurl'),
    path('all/', views.showAllPagePlaces, name = 'showAllPagePlaces'),  #переделать (делал просто чтобы иметь представление, если сменить name то отвалятся ссылки в меню)
    path('<str:url>/', views.viewPagePlaces, name = 'PagePlaces'),
]

