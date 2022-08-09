from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.shortcuts import reverse
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.

from datetime import datetime
import os
import time

def icon_place(instance, filename):
    ext = os.path.splitext(filename)
    current_datetime = datetime.now()
    file =  f"{current_datetime.day}-{current_datetime.month}-{current_datetime.year}-{int(time.time())}{ext[1]}"
    return f"user_{instance.id_user.id}_{instance.id_user.username}/icon/{file}"

class Icon(models.Model):
    name = models.CharField(name = 'name', max_length = 150, default = '')
    icon = models.FileField(upload_to = 'icons/', null = True, blank=True)
    is_deleted = models.BooleanField('is_deleted', default = False)

    def __str__(self):
        return f"{self.name} {self.is_deleted}"

    class Meta:
        verbose_name = 'Icon'
        verbose_name_plural = 'Icons'

class PagePlaces(models.Model):
    id_user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(name = 'name', max_length = 150, default = '')
    content = RichTextUploadingField(blank = True, null = True)
    short_info = models.CharField(name = 'short_info', max_length = 200, default = '')
    url = models.CharField(name = 'url', max_length = 20, unique = True)
    lat = models.DecimalField(name = 'lat', max_digits=19, decimal_places=16, null = True, blank=True)
    lng = models.DecimalField(name = 'lng', max_digits=19, decimal_places=16, null = True, blank=True)
    #icon = models.FileField(upload_to = icon_place, null = True, blank=True)
    icon_id = models.ForeignKey(Icon, on_delete = models.DO_NOTHING, null = True)
    is_deleted = models.BooleanField('is_deleted', default = False)

    def __str__(self):
        return f"{self.id} {self.id_user} {self.name} {self.short_info} {self.url} {self.is_deleted}"
    
    def get_absolute_url (self):
        return reverse('PagePlaces', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'page places'
        verbose_name_plural = 'page places'


class Feedback(models.Model):
    id_user = models.ForeignKey(User, on_delete = models.CASCADE)
    id_pageplace = models.ForeignKey(PagePlaces, on_delete = models.CASCADE)
    rating = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default = 0)
    content = models.TextField(max_length = 1000, null = True)
    date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField('is_deleted', default = False)

    def __str__(self):
        return f"{self.id} {self.rating} {self.date} {self.is_deleted}"
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
