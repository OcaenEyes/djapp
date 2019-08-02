from django.db import models

# Create your models here.
class MaterialInfo(models.Model):
    class Meta:
        verbose_name = "素材管理"
        verbose_name_plural = "素材管理"
    id = models.AutoField(primary_key=True)
    material_id = models.CharField(max_length=100,verbose_name="素材编码")
    material_pic = models.FileField(verbose_name="素材图片")
    material_text = models.CharField(max_length=250,verbose_name="素材文案")
    material_stime = models.DateTimeField(verbose_name="素材开始时间")
    material_etime = models.DateTimeField(verbose_name="素材结束时间")
    create_time = models.DateTimeField(verbose_name="创建时间")
    create_user = models.CharField(max_length=20,verbose_name="创建人")
    update_time = models.DateTimeField(verbose_name="更新时间")
    update_user = models.CharField(max_length=20,verbose_name="更新人")
