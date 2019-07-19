from django.contrib import admin
from .models import UserInfo
# Register your models here.
class UserInfoManage(admin.ModelAdmin):
    list_display = ('uaername','accountNo','password','headImg')

admin.site.register(UserInfo,UserInfoManage)