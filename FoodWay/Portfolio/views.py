from django.shortcuts import render

from datetime import datetime

def profile(request):
    context = { 
        'title' : 'Профиль',
        'year' : datetime.now().year,
    }
    return render(request,'Portfolio/profile.html', context)

def edit_profile(request):
    return render(request,'Portfolio/form.html')
