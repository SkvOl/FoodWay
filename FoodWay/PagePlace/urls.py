from django.urls import path
from . import views

urlpatterns = [
    path('addway/', views.add_way, name = 'add_way'),
    path('saveway/', views.save_way, name = 'save_way'),
    path('test/', views.test),
    path('getroutecar/', views.get_route_car, name = 'get_route_car'),
]
