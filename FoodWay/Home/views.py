"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.core import mail
from .forms import CustomUserCreationForm 
from .models import MyUser
import re

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'Home/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'Home/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'Home/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def register(request):       
    if request.method == 'POST': 
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid(): 
            try:
                date = form.cleaned_data
                MyUser.createUser(date['username'], date['email'], date['password1'])
                MyUser.loginUser(request = request, username = date['username'], password = date['password1']) 
                return redirect('home')
            except Exception as ex:
                print(ex)
        else:
            print("Форма не валидна")
            print(form.is_valid())
    else: 
        form = CustomUserCreationForm()
        print("Метод не post")
        print(request.method)

    context = { 
        'title' : 'register',
        'form' : form,
        'year' : datetime.now().year,
    } 

    return render(request,'Home/register.html', context)

def profile(request):
    context = { 
        'title' : 'Профиль',
        'year' : datetime.now().year,
    }
    return render(request,'Home/profile.html', context)
    
def page_not_found(request, exception):   
    print("error 40404")
    return render(request, 'Home/page_not_found.html', status=404)