from .models import *
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
# Create your views here.


def test(request):

    sql = 'SELECT `id`,`id_user`,`way` FROM `way_ways`'

    lis = db.getListData(ways,sql,['id','id_user','way'])
    
    print(lis[0]['id'])
    #way = {
    #    "1":"1",
    #    "2":"2"
    #    }

    #db.saveData(ways,id_user = 3, way = way, rating = 1, show = False, is_deleted = False)

    return redirect('home')

def add_way(request):
    if request.method == 'POST':
        ways.saveData(id_user = request.user.id, name = request.POST.dict()['name'], way = request.POST.dict()['GEOjson'], rating = 0, show = False, is_deleted = False)
        return JsonResponse({'stasus':'ok'}, safe=False)
    else:  
        current_user = request.user
        return render(request,'Way/form.html')

def save_way(request):
    if request.method == 'POST':
        dict_my = request.POST.dict()
        print(request.POST.dict())
       
        
        return JsonResponse({'stasus':'ok'}, safe=False)
        
