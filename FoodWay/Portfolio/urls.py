from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name = 'my_profile'),
    path('<str:url>', views.profile, name = 'profile_id'),
    path('edit/', views.edit_profile, name = 'edit_my_profile'),
    path('<str:url>/edit/', views.edit_profile, name = 'edit_profile_id'),
    path('edit_photo/<int:id_user>/', views.edit_photo, name = 'edit_photo'),
    path('checkurl/', views.checkURL, name = 'checkURL_profile'),
]

