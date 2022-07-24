from django.shortcuts import render
from .forms import FormProfile

from datetime import datetime

def profile(request):
    context = { 
        'title' : 'Профиль',
        'year' : datetime.now().year,
    }
    return render(request,'Portfolio/profile.html', context)

def handle_uploaded_file(f):
    with open('name.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def edit_profile(request):

    #вытащить из бд данные пользователя
    if request.method == 'POST':
        test = FormProfile(request.POST)
        #print(request.FILES)
        #handle_uploaded_file(request.FILES['image_profile'])
    else:
        test = FormProfile()
    print(test)
    context = { 
        'form' : test,
        'title' : 'Редактирование профиля',
        'year' : datetime.now().year,
    }
    return render(request,'Portfolio/form.html', context)
