from django.urls import include, path, re_path
from django.contrib import admin
from django.views.static import serve 
from . import settings


urlpatterns = [
    path('', include('Home.urls')),
    path('way/', include('Way.urls')),
    path('profile/', include('Portfolio.urls')),
    path('admin/', admin.site.urls),
    #re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

handler404 = "FoodWay.views.page_not_found"