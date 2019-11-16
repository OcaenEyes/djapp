from django.db import models
from rest_framework.views import APIView

# Create your models here.

class Zhihu(models.Model):
    id = models.IntegerField(blank=True, null=False,primary_key=True)
    question = models.CharField(max_length=254, blank=True, null=True)
    username = models.CharField(max_length=254, blank=True, null=True)
    userimage = models.CharField(max_length=254, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    favour = models.IntegerField(blank=True, null=True)
    ctime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zhihu'
        verbose_name = '知乎答案'
        verbose_name_plural = '知乎答案'
