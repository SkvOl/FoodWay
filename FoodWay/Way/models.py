from django.db import models
from django.http import JsonResponse
from jsonfield import JSONField
import json


class user_to_way(models.Model):
    id_user = models.PositiveIntegerField('id_user')
    way = JSONField('way')
    rating = models.PositiveSmallIntegerField('rating')
    show = models.BooleanField('show')
    is_deleted = models.BooleanField('is_deleted')

    def __str__(self):
        return f"{self.id} {self.id_user} {self.way} {self.rating} {self.show} {self.is_deleted}"

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

    class Meta:
        verbose_name = 'user_to_way'
        verbose_name_plural = 'user_to_way'

#class way(models.Model):
#    id_user = models.PositiveIntegerField('id_user')
#    name_way = models.CharField(max_length=30)
#    GeoJSON_lines = JSONField('GeoJSON_lines')
#    is_deleted = models.BooleanField('is_deleted')

#    def __str__(self):
#        return f"{self.id} {self.id_user} {self.name_way} {self.GeoJSON_lines} {self.is_deleted}"

#    class Meta:
#        verbose_name = 'way'
#        verbose_name_plural = 'way'

class way_to_comm(models.Model):
    id_user = models.PositiveIntegerField('id_user')
    id_way = models.PositiveIntegerField('id_way')
    comment = models.TextField('comment')
    is_deleted = models.BooleanField('is_deleted')

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

    class Meta:
        verbose_name = 'way_to_comm'
        verbose_name_plural = 'way_to_comm'


class rating(models.Model):
    id_user = models.PositiveIntegerField('id_user')
    id_way = models.PositiveIntegerField('id_way')
    value = models.PositiveSmallIntegerField('value')
    is_deleted = models.BooleanField('is_deleted')

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

    class Meta:
        verbose_name = 'rating'
        verbose_name_plural = 'rating'


