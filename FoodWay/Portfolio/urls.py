from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name = 'my_profile'),
    path('<int:id_user>', views.profile, name = 'profile_id'),
    path('edit/', views.edit_profile, name = 'edit_my_profile'),
    path('<int:id_user>/edit/', views.edit_profile, name = 'edit_profile_id'),
    
]

