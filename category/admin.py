from django.contrib import admin

from category.models import Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'image', 'is_active', 'meta_keyword')
    prepopulated_fields = {'slug': ('name',)}