from django.contrib import admin
from materialMana.models import MaterialInfo
# Register your models here.

class MaterialInfoManage(admin.ModelAdmin):
    list_display = ('material_id','material_pic','material_text','material_stime','material_etime','create_time','create_user','update_time')

admin.site.register(MaterialInfo,MaterialInfoManage)