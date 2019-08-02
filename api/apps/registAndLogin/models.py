from django.db import models

# Create your models here.

class UserInfo(models.Model):
    class Meta:
        verbose_name='用户信息'
        verbose_name_plural = '用户信息'

    id = models.AutoField(primary_key=True)
    uaername = models.CharField(max_length=100,null=True,db_column='username',verbose_name='账号')
    accountNo = models.IntegerField(db_column='accountNo',verbose_name="户头号")
    password = models.CharField(max_length=100,null=True,db_column='password',verbose_name='密码')

class UserDetial(models.Model):
    class Meta:
        verbose_name = "用户详情"
        verbose_name_plural = "用户详情"

    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=100,verbose_name="昵称",db_column='nickname')
    headImg = models.CharField(max_length=200, null=True, db_column='headImg', verbose_name='头像')
    email = models.EmailField(verbose_name="邮箱",db_column='email')
    age = models.IntegerField(verbose_name="年龄",db_column='age')
    birthyear = models.IntegerField(verbose_name="出生年",db_column='birthyear')
    birthmon = models.IntegerField(verbose_name="出生月",db_column='birthmon')
    birthday = models.IntegerField(verbose_name="出生日",db_column='birthday')
    adress = models.CharField(verbose_name="地址",max_length=250,db_column='adress')


