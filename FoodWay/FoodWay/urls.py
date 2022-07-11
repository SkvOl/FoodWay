"""
Definition of urls for FoodWay.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from Home import forms
import Home.views as home_viev
import Way.views as way_view


urlpatterns = [
    path('', home_viev.home, name='home'),
    path('contact/', home_viev.contact, name='contact'),
    path('about/', home_viev.about, name='about'),
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
    path('reg/', home_viev.register, name='reg'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),   
    path('admin/', admin.site.urls),
    path('profile/', home_viev.profile, name = 'profile'),
    path('test/', way_view.test),
]