from django.contrib import admin
from .models import UserInfo
# Register your models here.
class UserInfoManage(admin.ModelAdmin):
    list_display = ('uaername','accountNo','password','headImg')

admin.site.register(UserInfo,UserInfoManage)
admin.site.site_title="这是一个网站后台"
admin.site.site_header="这是一个网站后台biaoti"
admin.site.index_title="这是一个网站后台"