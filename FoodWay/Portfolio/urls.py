from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name = 'profile'),
    path('<int:id_user>', views.profile, name = 'profile'),
    path('edit/', views.edit_profile, name = 'edit_profile'),
    path('<int:id_user>/edit/', views.edit_profile, name = 'edit_profile'),
    
]

