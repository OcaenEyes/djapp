from django.db import models

# Create your models here.

class UserInfo(models.Model):
    class Meta:
        verbose_name='用户信息'
        verbose_name_plural = '用户信息'

    id = models.AutoField(primary_key=True)
    uaername = models.CharField(max_length=100,null=True,db_column='username',verbose_name='账号')
    accountNo = models.IntegerField(default=00000000)
    password = models.CharField(max_length=100,null=True,db_column='password',verbose_name='密码')
    headImg = models.CharField(max_length=200,null=True,db_column='headImg',verbose_name='头像')

