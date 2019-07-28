from django.db import models

# Create your models here.
class material_info(models.Model):
    id = models.AutoField(primary_key=True)
    material_id = models.CharField()
    # material_pic = models.
    # material_text
    # material_stime
    # material_etime
