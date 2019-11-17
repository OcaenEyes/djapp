from django.contrib import admin
from .models import Resume,Skills,Education,Projects,Blogs

# Register your models here.

# class ZhihuAdmin(admin.ModelAdmin):
#     list_display = ('id','question','username','content','favour','ctime')

admin.site.register(Resume)
admin.site.register(Skills)
admin.site.register(Education)
admin.site.register(Projects)
admin.site.register(Blogs)
admin.site.site_title = "ysilhouette"
admin.site.site_header = "乔克叔叔杂货店"
