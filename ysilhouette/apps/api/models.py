from django.db import models
from rest_framework.views import APIView


# Create your models here.

# class Zhihu(models.Model):
#     id = models.IntegerField(blank=True, null=False,primary_key=True)
#     question = models.CharField(max_length=254, blank=True, null=True)
#     username = models.CharField(max_length=254, blank=True, null=True)
#     userimage = models.CharField(max_length=254, blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     favour = models.IntegerField(blank=True, null=True)
#     ctime = models.DateField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'zhihu'
#         verbose_name = '知乎答案'
#         verbose_name_plural = '知乎答案'

class Resume(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=5, verbose_name="姓名")
    phone = models.CharField(max_length=11,verbose_name="手机")
    email = models.EmailField(verbose_name="邮箱")
    blog = models.CharField(max_length=200, verbose_name="博客")
    website = models.CharField(max_length=200, verbose_name="网站")

    class Meta:
        verbose_name = "个人简介"
        verbose_name_plural = "个人简介"

    def __str__(self):
        return self.name


class Skills(models.Model):
    sid = models.ForeignKey(Resume, on_delete=models.DO_NOTHING, verbose_name="姓名")
    skill = models.CharField(max_length=100, verbose_name="技能")
    pid = models.ForeignKey('self', verbose_name="技能点",on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "技能"
        verbose_name_plural = "技能"

    def __str__(self):
        return self.skill


class Education(models.Model):
    e_id = models.ManyToManyField(Resume, verbose_name="姓名")
    e_name = models.CharField(max_length=50, verbose_name="学校名称")
    e_major = models.CharField(max_length=50, verbose_name="专业")
    e_sdate = models.DateField(verbose_name="开始时间")
    e_edate = models.DateField(verbose_name="结束时间")

    class Meta:
        verbose_name = "教育经历"
        verbose_name_plural = "教育经历"

    def __str__(self):
        return self.e_name


class Projects(models.Model):
    p_id = models.ForeignKey(Resume, verbose_name="姓名",on_delete=models.DO_NOTHING)
    p_name = models.CharField(max_length=50, verbose_name="项目名称")
    p_sdate = models.DateField(verbose_name="开始时间")
    p_edate = models.DateField(verbose_name="结束时间")
    p_content = models.TextField(verbose_name="项目简介")

    class Meta:
        verbose_name = "项目经验"
        verbose_name_plural = "项目经验"

    def __str__(self):
        return self.p_name


class Blogs(models.Model):
    blog_id = models.AutoField(primary_key=True, editable=False)
    blog_title = models.CharField(max_length=50,verbose_name="标题")
    blog_content = models.TextField(verbose_name="内容")
    blog_editor = models.ForeignKey(Resume, on_delete=models.DO_NOTHING, verbose_name="作者")
    blog_ctime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    blog_utime = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "博客文章"
        verbose_name_plural = "博客文章"

    def __str__(self):
        return self.blog_title

