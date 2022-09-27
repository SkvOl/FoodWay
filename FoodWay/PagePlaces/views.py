from django.shortcuts import render, redirect
from .forms import PagePlacesForm, FeedbackForm
from FoodWay.views import page_not_found
from .models import PagePlaces, Icon, Feedback
from django.http import JsonResponse

from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from django.template.loader import render_to_string
from django.utils.formats import localize
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required

@login_required
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

@login_required
def editPagePlace(request, slug):
    """страница редактирования, PagePlaces"""

    page_place = get_object_or_404(PagePlaces, url = slug)
    all_icon = Icon.objects.filter(is_deleted = 0)
    
    if request.method == 'POST':
        form = PagePlacesForm(request.POST, instance = page_place) 
        if form.is_valid(): 
            form.save();
            return redirect(page_place.get_absolute_url())
    else:
        form = PagePlacesForm(instance = page_place)
    context = {
                'title' : f"Редактирование {page_place.name}",
                'all_icon' : all_icon,
                'form' : form,
                'selected_icon': page_place.icon_id
              }

    return render(request, 'PagePlaces/form.html', context)


def my_list(request):
    new_feed_vl = PagePlaces.objects.filter(lng__range = (request.POST.get('west'),request.POST.get('east')), lat__range = (request.POST.get('south'),request.POST.get('north')))
    new_feed = []
    
    #for i in range(50):
    for nf in new_feed_vl:
        new_feed.append({ 'id':nf.id, 'lat' : nf.lat, 'lng' : nf.lng, 'name' : nf.name, 'icon' : nf.icon_id.icon.url });

    return new_feed


def getpoints(request):
    data = my_list(request)
    return JsonResponse({'status' : True, 'data': data}, safe=False)

def getinfo_f(id):
    obj = PagePlaces.objects.get(pk = id)
    
    context = {
                'obj' : obj,
                'count_feedback' : Feedback.objects.filter(id_pageplace__id = id, is_deleted = False).count()
              }
    
    return render_to_string('PagePlaces/popup_marker.html', context)

def getinfo(request):
    return JsonResponse({'status' : True, 'data': getinfo_f(request.POST.get('id'))}, safe=False)

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

@login_required
def saveFeedback(request):
    if request.user.is_authenticated and request.method == 'POST':
        id_page = request.POST.get('id_pageplace')

        old_feedbacks = Feedback.objects.filter(id_user = request.user, id_pageplace = id_page, is_deleted = False)
        old_date = False
        if old_feedbacks:
            old_date = old_feedbacks[0].date
            old_feedbacks.update(is_deleted = True)

        obj = FeedbackForm(request.POST).save(commit=False)
        obj.id_user = request.user
        if old_date:
            obj.date = old_date
        
        obj.id_pageplace = PagePlaces.objects.get(pk=id_page)
        obj.save()
        return redirect(obj.id_pageplace.get_absolute_url())
    return redirect('home')
    #return JsonResponse({'status' : 1, 'date' : localize(obj.date)}, safe=False)

#def checkNewFeedback(request):
#    count = request.POST.get('count')
#    #reply_feed = request.POST.get('reply_feed')
#    if count or (count == 0):
#        id_pageplace = request.POST.get('id_pageplace')
#        new_count = Feedback.objects.filter(id_pageplace__id = id_pageplace).count()
#        delta = new_count - int(count)
#        if delta != 0:
#            #new_feed = Feedback.objects.filter(id_pageplace__id = id_pageplace).order_by('-date')[:delta].values_list('id_user__username', 'id_user__user_info__image_profile', 'content', 'rating', 'date')
            
#            new_feed = my_list(id_pageplace, delta)
#            return JsonResponse({'has_new' : True, 'new_feed' : new_feed, 'new_count' : new_count }, safe = False)
        


@login_required
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
        if(self.request.user.is_authenticated):
            query = Feedback.objects.filter(id_user = self.request.user, id_pageplace=self.object, is_deleted = False)
            if(query.exists()):
                context['form_comment'] = FeedbackForm(instance = query[0])
            else:
                context['form_comment'] = FeedbackForm()
        context['range'] = range(5)
        context['countOfFeed'] = self.object.feedback_set.count()

        feedback_list = self.object.feedback_set.filter(is_deleted = False).order_by('-date')
        paginator = Paginator(feedback_list, 2)

        page_number = self.request.GET.get('page')
        if(not page_number):
            page_number = 1
        context['page_range'] = paginator.get_elided_page_range(page_number, on_each_side=1, on_ends=1)
        context['curr_page'] = paginator.get_page(page_number)
        return context
