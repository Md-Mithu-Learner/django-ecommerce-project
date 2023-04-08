from django.contrib import admin

# Register your models here.
from django.contrib import admin
from App_Login.models import User, Profile

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'created_at', 'modified_at',)
#     search_fields = ('title',)
#     # list_per_page = 5

admin.site.register([User])
admin.site.register([Profile])
