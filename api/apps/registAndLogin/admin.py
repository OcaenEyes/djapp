from django.contrib import admin
from registAndLogin.models import UserInfo,UserDetial
# Register your models here.
class UserInfoManage(admin.ModelAdmin):
    list_display = ('uaername','accountNo','password')

class UserDetialManage(admin.ModelAdmin):
    list_display = ('nickname', 'email', 'age', 'adress')


admin.site.register(UserInfo,UserInfoManage)
admin.site.register(UserDetial,UserDetialManage)
admin.site.site_title="OCEANEYES-GZY"
admin.site.site_header="OCEANEYES-GZY"
admin.site.index_title="OCEANEYES-GZY"