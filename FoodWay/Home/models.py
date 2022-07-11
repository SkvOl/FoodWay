from django.db import models
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your models here.

class MyUser:
    def loginUser(request, username, password=None):
        user = authenticate(request = request, username = username, password = password)
        if user != '':
            print("Точно вошёл")
            login(request, user)
        else:
            print("Не вошёл")

    def createUser(username, email, password):
         user = User.objects.create_user(username, email, password)
         user.save()

