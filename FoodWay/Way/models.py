from django.db import models
from django.http import JsonResponse
from jsonfield import JSONField

from ckeditor.fields import RichTextField


class PagePlace(models.Model):
    content = RichTextField(blank=True, null=True)
    #name = models.CharField('name', max_length = 150, default = '')

    def __str__(self):
        return "test"


class ways(models.Model):
    id_user = models.PositiveIntegerField('id_user', default = 0)
    name = models.CharField('name', max_length = 150, default = '')
    way = JSONField('way')
    rating = models.PositiveSmallIntegerField('rating', default = 0)
    show = models.BooleanField('show', default = False)
    is_deleted = models.BooleanField('is_deleted', default = False)

    def __str__(self):
        return f"{self.id} {self.id_user}  {self.name} {self.way} {self.rating} {self.show} {self.is_deleted}"

    def getListData(sql, bones):
        item = user_to_way.objects.raw(sql)
        res = {}
        try:
            for i in range(len(item)):
                temp_res = {}
                for bon in bones:
                    if bon == 'id':
                        temp_res[bon] = item[i].id
                    elif bon =='id_user':
                        temp_res[bon] = item[i].id_user
                    elif bon =='way':
                        temp_res[bon] = item[i].way
                    elif bon =='rating':
                        temp_res[bon] = item[i].rating
                    elif bon =='show':
                        temp_res[bon] = item[i].show
                    elif bon =='is_deleted':
                        temp_res[bon] = item[i].is_deleted
                res[i] = temp_res
        except Exception as ex:
            print(ex)
        temp_res = {}
        return JsonResponse(res)

    def getOneData(sql, bones):
        item = user_to_way.objects.raw(sql)[0]
        res = {}
        try: 
            temp_res = {}
            for bon in bones:
                if bon == 'id':
                    temp_res[bon] = item.id
                elif bon =='id_user':
                    temp_res[bon] = item.id_user
                elif bon =='way':
                    temp_res[bon] = item.way
                elif bon =='rating':
                    temp_res[bon] = item.rating
                elif bon =='show':
                    temp_res[bon] = item.show
                elif bon =='is_deleted':
                    temp_res[bon] = item.is_deleted
            res[0] = temp_res
        except Exception as ex:
            print(ex)
        temp_res = {}
        return JsonResponse(res)

    def saveData(id_user, name, way, rating, show = False, is_deleted = False):
        ways.objects.create(id_user = id_user, name = name, way = way, rating = rating, show = show, is_deleted = is_deleted)
        
    class Meta:
        verbose_name = 'ways'
        verbose_name_plural = 'ways'


class user_to_way(models.Model):
    id_user = models.PositiveIntegerField('id_user', default = 0)
    id_way = models.PositiveIntegerField('id_way', default = 0)
    is_deleted = models.BooleanField('is_deleted', default = False)

    def __str__(self):
        return f"{self.id} {self.id_user} {self.id_way} {self.is_deleted}"

    def getListData(sql, bones):
        item = user_to_way.objects.raw(sql)
        res = {}
        try:
            for i in range(len(item)):
                temp_res = {}
                for bon in bones:
                    if bon == 'id':
                        temp_res[bon] = item[i].id
                    elif bon =='id_user':
                        temp_res[bon] = item[i].id_user
                    elif bon =='id_way':
                        temp_res[bon] = item[i].id_way
                    elif bon =='is_deleted':
                        temp_res[bon] = item[i].is_deleted
                res[i] = temp_res
        except Exception as ex:
            print(ex)
        temp_res = {}
        return JsonResponse(res)

    def getOneData(sql, bones):
        item = user_to_way.objects.raw(sql)[0]
        res = {}
        try: 
            temp_res = {}
            for bon in bones:
                if bon == 'id':
                    temp_res[bon] = item.id
                elif bon =='id_user':
                    temp_res[bon] = item.id_user
                elif bon =='id_way':
                    temp_res[bon] = item.id_way
                elif bon =='is_deleted':
                    temp_res[bon] = item.is_deleted
            res[0] = temp_res
        except Exception as ex:
            print(ex)
        temp_res = {}
        return JsonResponse(res)

    def saveData(id_user, id_way, is_deleted):
        ways.objects.create(id_user = id_user, id_way = id_way, is_deleted = is_deleted)

    class Meta:
        verbose_name = 'user_to_way'
        verbose_name_plural = 'user_to_way'


class way_to_comm(models.Model):
    id_user = models.PositiveIntegerField('id_user', default = 0)
    id_way = models.PositiveIntegerField('id_way', default = 0)
    comment = models.TextField('comment')
    is_deleted = models.BooleanField('is_deleted', default = False)

    def __str__(self):
        return f"{self.id} {self.id_user} {self.id_way} {self.comment} {self.is_deleted}"

    def getListData(sql, bones):
        item = user_to_way.objects.raw(sql)
        res = {}
        try:
            for i in range(len(item)):
                temp_res = {}
                for bon in bones:
                    if bon == 'id':
                        temp_res[bon] = item[i].id
                    elif bon =='id_user':
                        temp_res[bon] = item[i].id_user
                    elif bon =='id_way':
                        temp_res[bon] = item[i].id_way
                    elif bon =='comment':
                        temp_res[bon] = item[i].comment
                    elif bon =='is_deleted':
                        temp_res[bon] = item[i].is_deleted
                res[i] = temp_res
        except Exception as ex:
            print(ex)
        temp_res = {}
        return JsonResponse(res)

    def getOneData(sql, bones):
        item = user_to_way.objects.raw(sql)[0]
        res = {}
        try: 
            temp_res = {}
            for bon in bones:
                if bon == 'id':
                    temp_res[bon] = item.id
                elif bon =='id_user':
                    temp_res[bon] = item.id_user
                elif bon =='id_way':
                    temp_res[bon] = item.id_way
                elif bon =='comment':
                    temp_res[bon] = item.comment
                elif bon =='is_deleted':
                    temp_res[bon] = item.is_deleted
            res[0] = temp_res
        except Exception as ex:
            print(ex)
        temp_res = {}
        return JsonResponse(res)

    def saveData(id_user, id_way, comment, is_deleted):
        ways.objects.create(id_user = id_user, id_way = id_way, comment = comment, is_deleted = is_deleted)

    class Meta:
        verbose_name = 'way_to_comm'
        verbose_name_plural = 'way_to_comm'


class rating(models.Model):
    id_user = models.PositiveIntegerField('id_user', default = 0)
    id_way = models.PositiveIntegerField('id_way', default = 0)
    value = models.PositiveSmallIntegerField('value', default = 0)
    is_deleted = models.BooleanField('is_deleted', default = False)

    def __str__(self):
        return f"{self.id} {self.id_user} {self.id_way} {self.value} {self.is_deleted}"

    def getListData(sql, bones):
        item = user_to_way.objects.raw(sql)
        res = {}
        try:
            for i in range(len(item)):
                temp_res = {}
                for bon in bones:
                    if bon == 'id':
                        temp_res[bon] = item[i].id
                    elif bon =='id_user':
                        temp_res[bon] = item[i].id_user
                    elif bon =='id_way':
                        temp_res[bon] = item[i].id_way
                    elif bon =='value':
                        temp_res[bon] = item[i].value
                    elif bon =='is_deleted':
                        temp_res[bon] = item[i].is_deleted
                res[i] = temp_res
        except Exception as ex:
            print(ex)
        temp_res = {}
        return JsonResponse(res)

    def getOneData(sql, bones):
        item = user_to_way.objects.raw(sql)[0]
        res = {}
        try: 
            temp_res = {}
            for bon in bones:
                if bon == 'id':
                    temp_res[bon] = item.id
                elif bon =='id_user':
                    temp_res[bon] = item.id_user
                elif bon =='id_way':
                    temp_res[bon] = item.id_way
                elif bon =='value':
                    temp_res[bon] = item.value
                elif bon =='is_deleted':
                    temp_res[bon] = item.is_deleted
            res[0] = temp_res
        except Exception as ex:
            print(ex)
        temp_res = {}
        return JsonResponse(res)

    def saveData(id_user, id_way, value, is_deleted):
        ways.objects.create(id_user = id_user, id_way = id_way, value = value, is_deleted = is_deleted)

    class Meta:
        verbose_name = 'rating'
        verbose_name_plural = 'rating'


class db:    
    def getListData(table, sql, bones):
        item = table.objects.raw(sql)
        res = {}
        try:
            for i in range(len(item)):
                temp_res = {}
                for bon in bones:
                    if bon == 'id':
                        temp_res[bon] = item[i].id
                    elif bon =='id_user':
                        temp_res[bon] = item[i].id_user
                    elif bon =='way':
                        temp_res[bon] = item[i].way
                    elif bon =='id_way':
                        temp_res[bon] = item[i].id_way
                    elif bon =='rating':
                        temp_res[bon] = item[i].rating
                    elif bon =='comment':
                        temp_res[bon] = item[i].comment
                    elif bon =='value':
                        temp_res[bon] = item[i].value
                    elif bon =='show':
                        temp_res[bon] = item[i].show
                    elif bon =='is_deleted':
                        temp_res[bon] = item[i].is_deleted
                res[i] = temp_res
        except Exception as ex:
            print(ex)
        temp_res = {}
        return JsonResponse(res)

    def getOneData(table, sql, bones):
        item = table.objects.raw(sql)[0]
        res = {}
        try: 
            temp_res = {}
            for bon in bones:
                if bon == 'id':
                    temp_res[bon] = item.id
                elif bon =='id_user':
                    temp_res[bon] = item.id_user
                elif bon =='way':
                    temp_res[bon] = item.way
                elif bon =='id_way':
                    temp_res[bon] = item.id_way
                elif bon =='rating':
                    temp_res[bon] = item.rating
                elif bon =='comment':
                    temp_res[bon] = item.comment
                elif bon =='value':
                    temp_res[bon] = item.value
                elif bon =='show':
                    temp_res[bon] = item.show
                elif bon =='is_deleted':
                    temp_res[bon] = item.is_deleted
            res[0] = temp_res
        except Exception as ex:
            print(ex)
        temp_res = {}
        return JsonResponse(res)
   