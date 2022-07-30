from django.shortcuts import render
from .forms import PagePlacesForm
from FoodWay.views import page_not_found
from .models import PagePlaces
from django.http import JsonResponse

def addPagePlaces(request):
    """страница создания, редактированя PagePlaces"""

    form = PagePlacesForm()

    context = {
                'form' : form,
              }

    return render(request, 'PagePlaces/form.html', context)

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

def checkURL(request):
    unique = True       #надо узнать уникальность
    return JsonResponse({'unique' : unique}, safe=False)

def showAllPagePlaces(request):
    #выбирать только страницы, принадлежащие определенному пользователю, возможно надо будет через url передавать id (/all/<int:id>)
    context = {
                'PagePlaces' : PagePlaces.objects.all(),
                }
    return render(request, 'PagePlaces/showAllPagePlaces.html', context)