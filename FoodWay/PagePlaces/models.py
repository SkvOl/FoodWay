from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.shortcuts import reverse
# Create your models here.


class PagePlaces(models.Model):
    id_user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(name = 'name', max_length = 150, default = '')
    content = RichTextUploadingField(blank = True, null = True)
    short_info = models.CharField(name = 'short_info', max_length = 200, default = '')
    url = models.CharField(name = 'url', max_length = 20, unique = True)
    is_deleted = models.BooleanField('is_deleted', default = False)

    def __str__(self):
        return f"{self.id} {self.id_user} {self.name} {self.content} {self.short_info} {self.url} {self.is_deleted}"
    
    def get_absolute_url (self):
        return reverse('PagePlaces', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'page places'
        verbose_name_plural = 'page places'
