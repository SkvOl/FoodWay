from django.shortcuts import render, redirect
from .models import user_to_way, way_to_comm, rating

from django.http import JsonResponse
# Create your views here.


def test(request):

    sql = 'SELECT `id`,`id_user`,`way` FROM `way_user_to_way`'

    lis = user_to_way.getOneData(sql,['id','id_user','way'])
    print(type(lis))

    print(lis)

    return redirect('home')

def add_way(request):
    if request.method == 'POST':
        return redirect('home')
    else:
        context = { 
            'test' : render(request,'Way/popup_marker.html'),
        } 
        return render(request,'Way/form.html',context)

def save_way(request):
    if request.method == 'POST':
        print(request.POST)
        return JsonResponse(request.POST.get('geoJSON'), safe=False)
        
