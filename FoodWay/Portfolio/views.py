from django.shortcuts import render
from .forms import FormProfile
from .models import User_info

from datetime import datetime

def profile(request, id_user=-1):
    if id_user == -1:
        id_user = request.user.id

    context = {
        'title' : 'Профиль',
        'year' : datetime.now().year,
    }
    return render(request,'Portfolio/profile.html', context)

def handle_uploaded_file(f):
    with open('name.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def edit_profile(request, id_user = -1):
    if id_user == -1:
        id_user = request.user.id

    #вытащить из бд данные пользователя
    if request.method == 'POST':
        test = request.POST
        print(test)
        User_info.saveData(request.user,test.get('firstname'),test.get('phone'),test.get('show_phone'),test.get('url_user'), 0, test.get('show_email'), 0, test.get('about_user'), False)
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
