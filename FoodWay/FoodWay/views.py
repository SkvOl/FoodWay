from django.shortcuts import render

def page_not_found(request, exception):   
    return render(request, 'page_not_found.html',{'title':'Страница не найдена'}, status=404)