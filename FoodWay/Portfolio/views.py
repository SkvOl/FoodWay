from django.shortcuts import redirect, render
from .forms import User_info_form
from .models import User_info

from django.contrib.auth.models import User

from datetime import datetime

def print_fields(model, par, val):
    print(model.objects.get(par = val)._meta.get_fields())

def profile(request, id_user=-1):
    if id_user == -1:
        id_user = request.user.id
    
    if id_user == request.user.id:
        is_owner = True
    else:
        is_owner = False

    show_all = is_owner or request.user.is_superuser
    #print("data: ")
    #print(User.objects.get(id = id_user).email)

    context = {
        'title' : 'Профиль',
        'year' : datetime.now().year,
        #'view_user' : User.objects.get(id = id_user),
        'dop_info' : User_info.objects.get(id_user__id = id_user),
        'show_all': show_all,
    }
    return render(request,'Portfolio/profile.html', context)

def handle_uploaded_file(f):
    with open('name.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def edit_profile(request, id_user = -1):
    if id_user == -1:
        id_user = request.user.id

    #print(User_info.objects.get(id_user__id = id_user)._meta.get_fields())

    #вытащить из бд данные пользователя
    if request.method == 'POST':
        form = User_info_form(request.POST)
        #print(request.POST.dict())
        #test = request.POST
        if form.is_valid():
            data = form.cleaned_data
            if User_info.objects.filter(id_user__id = id_user).exists():
                user_info = User_info.objects.get(id_user__id = id_user)
            else:
                user_info = User_info()
            print(data)
            user_info.id_user = User.objects.get(id = id_user)
            user_info.id_user.email = data['email']
            user_info.id_user.first_name = data['first_name']
            user_info.id_user.last_name = data['last_name']
            
            user_info.phone=data['phone']
            user_info.show_phone=data['show_phone']
            user_info.url_user=data['url_user']
            user_info.show_email=data['show_email']
            user_info.about_user=data['about_user']

            user_info.id_user.save()
            user_info.save()
        #print(test)
        #User_info.saveData(request.user,test.get('firstname'),test.get('phone'),test.get('show_phone'),test.get('url_user'), 0, test.get('show_email'), 0, test.get('about_user'), False)
        #print(request.FILES)
        #handle_uploaded_file(request.FILES['image_profile'])
        return redirect(f'profile/{id_user}')
    else:
        param={}
        if User.objects.filter(id = id_user).exists():
            user_model = User.objects.get(id = id_user)
            param |= user_model.__dict__
        if User_info.objects.filter(id_user__id = id_user).exists():
            user_info_model = User_info.objects.get(id_user__id = id_user)
            param |= user_info_model.__dict__
            
        #print(user_model.__dict__ | user_info_model.__dict__)
        form = User_info_form(param)

    context = { 
        'form' : form,
        'title' : 'Редактирование профиля',
        'year' : datetime.now().year,
    }
    return render(request,'Portfolio/form.html', context)
