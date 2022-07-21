from django.contrib import admin
from .models import user_to_way, way_to_comm, rating, ways, PagePlace

# Register your models here.

admin.site.register(user_to_way)
admin.site.register(way_to_comm)
admin.site.register(rating)
admin.site.register(ways)
admin.site.register(PagePlace)