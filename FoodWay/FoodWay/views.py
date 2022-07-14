from django.shortcuts import render

def page_not_found(request, exception):   
    print("error 40404")
    return render(request, 'page_not_found.html', status=404)