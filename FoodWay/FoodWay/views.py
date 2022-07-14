from django.shortcuts import render
from datetime import timedelta
from ratelimit.decorators import ratelimit
from blacklist.ratelimit import blacklist_ratelimited

@ratelimit(key='user_or_ip', rate='50/m', block=False)
@blacklist_ratelimited(timedelta(minutes=30))

def page_not_found(request, exception):   
    return render(request, 'page_not_found.html',{'title':'Страница не найдена'}, status=404)