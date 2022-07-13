"""
Definition of urls for FoodWay.
"""


from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('', include('Home.urls')),
    path('way/', include('Way.urls')),
    path('admin/', admin.site.urls),
]

handler404 = "FoodWay.views.page_not_found"