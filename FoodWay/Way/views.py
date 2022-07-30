from .models import *
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from .forms import name_of_Way
from .make_route import route

def test(request):

    #route(request)

    #sql = 'SELECT `id`,`id_user`,`way` FROM `way_ways`'

    #lis = db.getListData(ways,sql,['id','id_user','way'])
    
    #print(lis[0]['id'])
    ##way = {
    ##    "1":"1",
    ##    "2":"2"
    ##    }

    #db.saveData(ways,id_user = 3, way = way, rating = 1, show = False, is_deleted = False)

    return redirect('home')

def add_way(request):
    if request.method == 'POST':
        ways.saveData(id_user = request.user.id, name = request.POST.dict()['name'], way = request.POST.dict()['GEOjson'], rating = 0, show = False, is_deleted = False)
        return JsonResponse({'stasus':'ok'}, safe=False)
    else:  
        form = name_of_Way()
        #form2 = PagePlaceForm()
        
        return render(request,'Way/form.html',{'form':form})

def save_way(request):
    if request.method == 'POST':
        dict_my = request.POST.dict()
        print(request.POST.dict())
       
        
        return JsonResponse({'stasus':'ok'}, safe=False)

def get_route_car(request):
    item = request.POST.dict()
    item['data'] = json.loads(item['data'])
    item_new=[]
    for i in range(len(item['data']) - 1):
        item_new.append(item['data'][i] + item['data'][i + 1])

    return JsonResponse(route(request, item_new), safe=False)
        
