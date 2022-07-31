from django.shortcuts import render, redirect
from .forms import PagePlacesForm
from FoodWay.views import page_not_found
from .models import PagePlaces
from django.http import JsonResponse

def addPagePlaces(request):
    """страница создания, PagePlaces"""

    if request.method == 'POST': 
        form = PagePlacesForm(request.POST) 
        if form.is_valid(): 
            try:
                form.save(); 
                return redirect('home')
            except:
                print("Ошибка сохранения формы при добавлении PagePlaces")
    else:
        form = PagePlacesForm()


    context = {
                'form' : form,
              }

    return render(request, 'PagePlaces/form.html', context)

def editPagePlaces(request, id_PagePlace):
    """страница редактирования, PagePlaces"""


    if PagePlaces.objects.filter(id = id_PagePlace).exists():
        if request.method == 'POST': 
            form = PagePlacesForm(request.POST) 
            if form.is_valid(): 
                try:
                    form.save(); 
                    return redirect('home')
                except:
                    print("Ошибка сохранения формы при добавлении PagePlaces")
        else:
            user = PagePlaces.objects.get(id = id_PagePlace)
            initial = {
                        'name' : user.name,
                        'content' : user.content,
                        'short_info' : user.short_info,
                        'url' : user.url,
                      }

            form = PagePlacesForm(initial = initial)

    else:
        return page_not_found(request, None)



    context = {
                'form' : form,
              }

    return render(request, 'PagePlaces/edit.html', context)

def viewPagePlaces(request, url = ''):
    """страница просмотра PagePlaces"""

    if PagePlaces.objects.filter(url = url).exists():

        user_view = PagePlaces.objects.get(url = url)

        if user_view.id_user == request.user.id:
            is_owner = True
        else:
            is_owner = False

        show_all = is_owner or request.user.is_superuser
    
        context = {
                    'name' : user_view.name,
                    'url' : url,
                  }

        return render(request, 'PagePlaces/PagePlace.html', context)
    else:
        return page_not_found(request, None)

def checkURL(request, url = ''):
    unique = PagePlaces.objects.filter(url = url).exists()       #надо узнать уникальность
    return JsonResponse({'unique' : unique}, safe = False)

def showAllPagePlaces(request):
    #выбирать только страницы, принадлежащие определенному пользователю, возможно надо будет через url передавать id (/all/<int:id>)
    context = {
                'PagePlaces' : PagePlaces.objects.all(),
                }
    return render(request, 'PagePlaces/showAllPagePlaces.html', context)