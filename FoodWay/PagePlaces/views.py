from django.shortcuts import render, redirect
from .forms import PagePlacesForm
from FoodWay.views import page_not_found
from .models import PagePlaces
from django.http import JsonResponse

from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

def addPagePlaces(request):
    """страница создания, PagePlaces"""

    if request.method == 'POST': 
        form = PagePlacesForm(request.POST) 
        if form.is_valid(): 
            try:
                res = form.save(commit=False)
                res.id_user = request.user
                res.save()
                return redirect('home')
            except:
                print("Ошибка сохранения формы при добавлении PagePlaces")
    else:
        form = PagePlacesForm()


    context = {
                'form' : form,
              }

    return render(request, 'PagePlaces/form.html', context)

def editPagePlace(request, slug):
    """страница редактирования, PagePlaces"""

    page_place = get_object_or_404(PagePlaces, url = slug)

    if request.method == 'POST': 
        form = PagePlacesForm(request.POST) 
        if form.is_valid(): 
            #form.save(); 
            data = form.cleaned_data
            page_place.name = data['name']  #пришлось делать таким образом, так как иначе создается измененная копия (из за отсутствия id в форме)
            page_place.content = data['content']
            page_place.short_info = data['short_info']
            page_place.url = data['url']
            page_place.save()
            return redirect('home')
    else:
        form = PagePlacesForm(instance = page_place)

    context = {
                'form' : form,
              }

    return render(request, 'PagePlaces/form.html', context)

def checkURL(request):
    url = request.POST.get('url')
    id_PagePlaces = request.POST.get('id_PagePlaces')
    res = PagePlaces.objects.filter(url = url)

    if id_PagePlaces:
        res = res.exclude(id = id_PagePlaces)

    if res.exists():
        status = 1  #провал (не уникальный)
    else:
        status = 0
    return JsonResponse({'status' : status}, safe=False)

def deletePagePlace(request):
    id_PagePlaces = request.POST.get('id_PagePlaces')
    pageplace = PagePlaces.objects.get(id = id_PagePlaces)
    if pageplace.id_user == request.user or request.user.is_superuser:
        pageplace.is_deleted = True
        pageplace.save()
    return JsonResponse({'status' : '1'}, safe=False)

class PagePlaceList(ListView):
    model = PagePlaces
    context_object_name = 'PagePlaces'
    #template_name = 'PagePlaces/PagePlaces_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список страниц'
        return context

    def get_queryset(self):
        return PagePlaces.objects.all()

class PagePlaceDetailView(DetailView):
    model = PagePlaces
    context_object_name = 'PagePlace'
    slug_field = 'url'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context