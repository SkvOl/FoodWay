from django.db import models
from django.contrib.auth.models import User

class User_info(models.Model):

    id_user = models.OneToOneField(User, on_delete = models.CASCADE)

    first_name = models.CharField('first_name', max_length = 150, default = '')

    phone = models.CharField(max_length=13, default = '')

    show_phone = models.BooleanField(default = False)

    url_user = models.CharField(max_length=30, default = '')

    #email = models.EmailField()

    show_email = models.BooleanField(default = False)

    #image_profile = models.ImageField(upload_to="picture/")

    about_user = models.CharField(max_length=2000, default = '')

    is_deleted = models.BooleanField('is_deleted', default = False)

    def __str__(self):
        return f"{self.id} {self.first_name}  {self.phone} {self.is_deleted}"

    def saveData(id_user, first_name, phone, show_phone, url_user, email, show_email, image_profile, about_user, is_deleted = False):
        User_info.objects.create(id_user = id_user, first_name = first_name, phone = phone, show_phone = False, url_user = url_user, show_email = True, about_user = about_user, is_deleted = is_deleted)



