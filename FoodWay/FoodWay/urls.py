from django.urls import include, path, re_path
from django.contrib import admin
from django.views.static import serve 
from . import settings

from django.conf.urls.static import static

urlpatterns = [
    path('', include('Home.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    #path('way/', include('Way.urls')),
    path('profile/', include('Portfolio.urls')),
    path('pageplaces/', include('PagePlaces.urls')),
    path('jet/', include('jet.urls', 'jet')),  # URL-адреса Django JET
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "FoodWay.views.page_not_found"