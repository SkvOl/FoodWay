from django.urls import path
from . import views

urlpatterns = [
    path('addway/', views.add_way, name = 'add_way'),
    path('test/', views.test),
]

