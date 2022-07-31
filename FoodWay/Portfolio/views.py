from email.mime import image
from django.shortcuts import redirect, render
from django.http import JsonResponse
from .forms import User_info_form
from .models import User_info

from FoodWay.views import page_not_found

from django.contrib.auth.models import User

from datetime import datetime

def print_fields(model, par, val):
    print(model.objects.get(par = val)._meta.get_fields())

def profile(request, url = -1):
    if url == -1:
        url = request.user.id
    
    if User.objects.filter(url_user = url).exists():

        user_view = User.objects.get(url_user = url)

        if user_view.id_user == request.user.id:
            is_owner = True
        else:
            is_owner = False

        show_all = is_owner or request.user.is_superuser
    
        
        context = {
            'title' : 'Профиль',
            'year' : datetime.now().year,
            'dop_info' : User_info.objects.get_or_create(url = user_view.url_user)[0],#сомневаюсь что верно переправил функцию
            'show_all': show_all,
        }
        return render(request, 'Portfolio/profile.html', context)
    else:
        return page_not_found(request, None)

def handle_uploaded_file(f):
    with open('name.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def edit_profile(request, url = -1):
    
    if url == -1:
        url = request.user.id

    if User.objects.filter(url_user = url).exists():

        user_edit = User.objects.get(url_user = url)
        user_info = User_info.objects.get_or_create(url = user_edit)[0]     #не получилось создать через id_user_(два подчеркивания)_id (что логично в общем-то)
        
        if request.method == 'POST':
            form = User_info_form(request.POST)
            
            if form.is_valid():
                data = form.cleaned_data
                print(request.FILES)
                #print(data)
                #user_info.id_user = user_edit  #возможно надо
                user_info.url.email = data['email']
                user_info.url.first_name = data['first_name']
                user_info.url.last_name = data['last_name']
                
                user_info.phone = data['phone']               #возможно можно засунуть в конструктор
                user_info.show_phone = data['show_phone']
                #user_info.url_user = data['url_user']
                user_info.show_email = data['show_email']
                user_info.about_user = data['about_user']

                if request.FILES and request.FILES['image_profile']:
                    user_info.image_profile = request.FILES['image_profile'];
                
                user_info.url.save()
                user_info.save()

                return redirect(f"/profile/{url}")
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

def edit_photo(request, url = -1):
    if request.method == 'POST':    #по какой-то причина в jquery/ajax появляется ошибка
        if url == -1:
            url = request.user.id

        if User.objects.filter(url_user = url).exists():
            user_info = User_info.objects.get(url_user__id = url)

            if request.POST.get('delete')=='true':
                user_info.image_profile = None
                user_info.save()

            elif request.POST.get('delete')=='false' and request.FILES and request.FILES['image_profile']:
                user_info.image_profile = request.FILES['image_profile']
                user_info.save()

    return JsonResponse({'stasus':'ok'}, safe=False)
