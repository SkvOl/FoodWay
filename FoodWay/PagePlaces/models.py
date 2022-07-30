from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class PagePlaces(models.Model):
    id_user = models.PositiveIntegerField('id_user', default = 0)   #переделать на oneToOneField
    name = models.CharField(name = 'name', max_length = 150, default = '')
    content = RichTextUploadingField(blank = True, null = True)
    short_info = models.CharField(name = 'short_info', max_length = 200, default = '')
    url = models.CharField(name = 'url', max_length = 20, default = '')
    is_deleted = models.BooleanField('is_deleted', default = False)

    def __str__(self):
        return f"{self.id} {self.id_user} {self.name} {self.content} {self.short_info} {self.url} {self.is_deleted}"
    
    class Meta:
        verbose_name = 'page places'
        verbose_name_plural = 'page places'
