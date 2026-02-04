from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name_en", "type", "user", "is_default")
    list_filter = ("type", "is_default")
    search_fields = ("name_en", "name_uz", "name_ru")
