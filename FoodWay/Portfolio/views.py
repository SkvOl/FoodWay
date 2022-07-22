from django.shortcuts import render
from .forms import FormProfile

from datetime import datetime

def profile(request):
    context = { 
        'title' : 'Профиль',
        'year' : datetime.now().year,
    }
    return render(request,'Portfolio/profile.html', context)

def edit_profile(request):

    #вытащить из бд данные пользователя

    test = FormProfile()
    #print(test)
    context = { 
        'form' : test,
        'title' : 'Редактирование профиля',
        'year' : datetime.now().year,
    }
    return render(request,'Portfolio/form.html', context)
