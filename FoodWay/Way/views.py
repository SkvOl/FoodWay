from .models import user_to_way, way_to_comm, rating, ways
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
# Create your views here.


def test(request):

    #sql = 'SELECT `id`,`id_user`,`way` FROM `way_user_to_way`'

    #lis = ways.getOneData(sql,['id','id_user','way'])
    #print(type(lis))

    #print(lis)

    way = {
        "1":"1",
        "2":"2"
        }

    ways.saveData(id_user = 3, way = way, rating = 1, show = False, is_deleted = False)

    return redirect('home')

def add_way(request):
    if request.method == 'POST':
        ways.saveData(id_user = request.user.id, name = request.POST.dict()['name'], way = request.POST.dict()['GEOjson'], rating = 0, show = False, is_deleted = False)
        return JsonResponse({'stasus':'ok'}, safe=False)
    else:  
        current_user = request.user
        print(f"id current: {current_user.id}")
        return render(request,'Way/form.html')

def save_way(request):
    if request.method == 'POST':
        dict_my = request.POST.dict()
        print(request.POST.dict())
       
        
        return JsonResponse({'stasus':'ok'}, safe=False)
        
