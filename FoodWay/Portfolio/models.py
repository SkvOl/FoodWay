from django.db import models
from django.contrib.auth.models import User


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

from datetime import datetime
import os
import time

def user_path(instance, filename):
    ext = os.path.splitext(filename)
    current_datetime = datetime.now()
    file =  f"{current_datetime.day}-{current_datetime.month}-{current_datetime.year}-{int(time.time())}{ext[1]}"
    return f"user_{instance.id_user.id}_{instance.id_user.username}/{file}"

class User_info(models.Model):

    id_user = models.OneToOneField(User, on_delete = models.CASCADE)

    #first_name = models.CharField('first_name', max_length = 150, default = '')

    phone = models.CharField(max_length = 13, default = '')

    show_phone = models.BooleanField(default = False)

    url_user = models.CharField(max_length = 30, null=True)

    #email = models.EmailField()

    show_email = models.BooleanField(default = False)

    image_profile = models.FileField(upload_to=user_path, null=True)

    about_user = models.CharField(max_length = 2000, default = '')

    is_deleted = models.BooleanField('is_deleted', default = False)

    def __str__(self):
        return f"{self.id_user} {self.phone} {self.is_deleted}"

    def saveData(id_user, first_name, phone, show_phone, url_user, email, show_email, image_profile, about_user, is_deleted = False):
        User_info.objects.create(id_user = id_user, first_name = first_name, phone = phone, show_phone = False, url_user = url_user, show_email = True, about_user = about_user, is_deleted = is_deleted)



@receiver(post_save, sender=User)
def save_or_create_user_info(sender, instance, created, **kwargs):
    if created:
        User_info.objects.create(id_user = instance, url_user = f"p{instance.id}")
    else:
        try:
            instance.user_info.save()
        except ObjectDoesNotExist:
            User_info.objects.create(id_user = instance, url_user = f"p{instance.id}")