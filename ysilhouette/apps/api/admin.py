from django.contrib import admin
from .models import Zhihu

# Register your models here.

class ZhihuAdmin(admin.ModelAdmin):
    list_display = ('id','question','username','content','favour','ctime')

admin.site.register(Zhihu,ZhihuAdmin)
admin.site.site_title = "ysilhouette"
admin.site.site_header = "乔克叔叔杂货店"
