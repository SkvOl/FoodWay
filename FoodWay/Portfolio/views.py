from django.shortcuts import render
from .forms import FormProfile
from .models import User_info

from django.contrib.auth.models import User

from datetime import datetime

def checkbox(data):
    if data=='on':
        return True
    else:
        return False

def profile(request, id_user=-1):
    if id_user == -1:
        id_user = request.user.id

    print(User.objects.get(id = id_user))

    context = {
        'title' : 'Профиль',
        'year' : datetime.now().year,
        'view_user' : User.objects.get(id = id_user)
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
        form = FormProfile(request.POST)
        #print(request.POST.dict())
        #test = request.POST
        if form.is_valid():
            data = form.cleaned_data
            if User_info.objects.filter(id = id_user).exists():
                user_info = User_info.objects.get(id = id_user)
            else:
                user_info = User_info()
            user_info.id_user = User.objects.get(id = id_user)
            user_info.first_name=data['firstname']
            user_info.phone=data['phone']
            user_info.show_phone='show_phone' in data
            user_info.url_user=data['url_user']
            user_info.show_email='show_email' in data
            user_info.about_user=data['about_user']
            user_info.save()
        #print(test)
        #User_info.saveData(request.user,test.get('firstname'),test.get('phone'),test.get('show_phone'),test.get('url_user'), 0, test.get('show_email'), 0, test.get('about_user'), False)
        #print(request.FILES)
        #handle_uploaded_file(request.FILES['image_profile'])
    else:
        form = FormProfile()
        if User.objects.filter(id = id_user).exists():
            User_model = User.objects.get(id = id_user)
            form.email = User.email
        if User_info.objects.filter(id = id_user).exists():
            User_info_model = User_info.objects.get(id = id_user)
            #test.firstname.prepare_value(User_info_model.first_name)
            #test.phone = User_info_model.phone
            print(User_info_model)
        #test.firstname = 
    #print(test)
    context = { 
        'form' : form,
        'title' : 'Редактирование профиля',
        'year' : datetime.now().year,
    }
    return render(request,'Portfolio/form.html', context)
