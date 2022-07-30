from django.shortcuts import render
from .forms import PagePlacesForm
from FoodWay.views import page_not_found
from .models import PagePlaces

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
