from email.mime import image
from django.shortcuts import redirect, render
from .forms import User_info_form
from .models import User_info

from FoodWay.views import page_not_found

from django.contrib.auth.models import User

from datetime import datetime

def print_fields(model, par, val):
    print(model.objects.get(par = val)._meta.get_fields())

def profile(request, id_user=-1):
    if id_user == -1:
        id_user = request.user.id
    
    if User.objects.filter(id = id_user).exists():

        user_view = User.objects.get(id = id_user)

        if id_user == request.user.id:
            is_owner = True
        else:
            is_owner = False

        show_all = is_owner or request.user.is_superuser
    
        
        context = {
            'title' : 'Профиль',
            'year' : datetime.now().year,
            'dop_info' : User_info.objects.get_or_create(id_user = user_view)[0],
            'show_all': show_all,
        }
        return render(request, 'Portfolio/profile.html', context)
    else:
        return page_not_found(request, None)

def handle_uploaded_file(f):
    with open('name.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def edit_profile(request, id_user = -1):
    
    if id_user == -1:
        id_user = request.user.id

    if User.objects.filter(id = id_user).exists():

        user_edit = User.objects.get(id = id_user)
        user_info = User_info.objects.get_or_create(id_user = user_edit)[0]     #не получилось создать через id_user_(два подчеркивания)_id (что логично в общем-то)
        
        if request.method == 'POST':
            form = User_info_form(request.POST)
            
            if form.is_valid():
                data = form.cleaned_data
                print(request.FILES)
                #print(data)
                #user_info.id_user = user_edit  #возможно надо
                user_info.id_user.email = data['email']
                user_info.id_user.first_name = data['first_name']
                user_info.id_user.last_name = data['last_name']
                
                user_info.phone=data['phone']               #возможно можно засунуть в конструктор
                user_info.show_phone=data['show_phone']
                user_info.url_user=data['url_user']
                user_info.show_email=data['show_email']
                user_info.about_user=data['about_user']

                if request.FILES and request.FILES['image_profile']:
                    user_info.image_profile = request.FILES['image_profile'];
                
                user_info.id_user.save()
                user_info.save()

                return redirect(f"/profile/{id_user}")
            else:
                print(form)
        else:
            form = User_info_form(user_info.__dict__ | user_edit.__dict__)

        try:
            image_src =  user_info.image_profile.url
        except:
            image_src = None

        context = { 
            'form' : form,
            'id_view_user': user_edit.id,
            'title' : 'Редактирование профиля',
            'year' : datetime.now().year,
            'image_src' : image_src,
        }
        return render(request,'Portfolio/form.html', context)
    else:
        return page_not_found(request, None)

def edit_photo(request, id_user = -1):
    if request.method == 'POST':    #по какой-то причина в jquery/ajax появляется ошибка
        if id_user == -1:
            id_user = request.user.id

        if User.objects.filter(id = id_user).exists():
            user_info = User_info.objects.get(id_user__id = id_user)

            if request.POST.get('delete')=='true':
                user_info.image_profile = None
                user_info.save()
            elif request.POST.get('delete')=='false' and request.FILES and request.FILES['image_profile']:
                user_info.image_profile = request.FILES['image_profile']
                user_info.save()

    return JsonResponse({'stasus':'ok'}, safe=False)
