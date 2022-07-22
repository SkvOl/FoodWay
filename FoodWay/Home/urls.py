from django.contrib.auth.views import LoginView, LogoutView
from datetime import datetime
from django.urls import path
from . import views
from . import forms

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='Home/login.html',
             authentication_form = forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('reg/', views.register, name='reg'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    
]
