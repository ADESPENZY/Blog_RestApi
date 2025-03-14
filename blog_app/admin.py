from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Blog

# Register your models here.
class CustonUserAdmin(UserAdmin):
    list_display = ("username", "first_name", "last_name", "bio", "facebook", "instagram", "twitter", "youtube")

admin.site.register(CustomUser, CustonUserAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "is_draft", "category", "created_at")
admin.site.register(Blog, BlogAdmin)