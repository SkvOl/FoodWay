from django.shortcuts import render, redirect
from .forms import PagePlacesForm, FeedbackForm
from FoodWay.views import page_not_found
from .models import PagePlaces, Icon, Feedback
from django.http import JsonResponse

from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from django.template.loader import render_to_string
from django.utils.formats import localize

def addPagePlaces(request):
    """страница создания, PagePlaces"""
    all_icon = Icon.objects.filter(is_deleted = 0)
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
                'title' : 'Добавление страницы',
                'all_icon' : all_icon,
                'form' : form,
              }

    return render(request, 'PagePlaces/form.html', context)

def editPagePlace(request, slug):
    """страница редактирования, PagePlaces"""

    page_place = get_object_or_404(PagePlaces, url = slug)
    all_icon = Icon.objects.filter(is_deleted = 0)
    
    if request.method == 'POST':
        form = PagePlacesForm(request.POST, instance = page_place) 
        if form.is_valid(): 
            form.save(); 
            #data = form.cleaned_data
            #page_place.name = data['name']  #пришлось делать таким образом, так как иначе создается измененная копия (из за отсутствия id в форме)
            #page_place.content = data['content']
            #page_place.short_info = data['short_info']
            #page_place.url = data['url']
            #page_place.save()
            return redirect('home')
    else:
        form = PagePlacesForm(instance = page_place)
    context = {
                'title' : f"Редактирование {page_place.name}",
                'all_icon' : all_icon,
                'form' : form,
                'selected_icon': page_place.icon_id
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

def saveFeedback(request):
    if(request.user.is_authenticated):
        obj = FeedbackForm(request.POST).save(commit=False)
        obj.id_user = request.user
        
        obj.id_pageplace = PagePlaces.objects.get(pk=request.POST.get('id_pageplace'))
        obj.save()
    return JsonResponse({'status' : 1, 'date' : localize(obj.date)}, safe=False)

def checkNewFeedback(request):
    count = request.POST.get('count')
    #reply_feed = request.POST.get('reply_feed')
    if count or (count == 0):
        id_pageplace = request.POST.get('id_pageplace')
        new_count = Feedback.objects.filter(id_pageplace__id = id_pageplace).count()
        delta = new_count - int(count)
        if delta != 0:
            new_feed = Feedback.objects.filter(id_pageplace__id = id_pageplace).order_by('-date')[:delta].values_list('id_user__username', 'id_user__user_info__image_profile', 'content', 'rating', 'date')
            return JsonResponse({'has_new':True, 'new_feed' : list(new_feed), 'new_count':new_count }, safe=False)

    return JsonResponse({'has_new':False, 'new_feed' : None }, safe=False)
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
        return PagePlaces.objects.filter(is_deleted = 0)

class PagePlaceDetailView(DetailView):
    model = PagePlaces
    context_object_name = 'PagePlace'
    slug_field = 'url'

    queryset = PagePlaces.objects.filter(is_deleted = False)

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        context['form_comment'] = FeedbackForm()
        context['range'] = range(5)
        context['countOfFeed'] = self.object.feedback_set.count()
        context['list_feedback'] = self.object.feedback_set.all().order_by('-date')
        return context
