from django.contrib import admin
from product.forms import ProductAdminForm

from product.models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    
    # sets values for how the admin site lists your products
    list_display = ('name', 'price', 'sale_price', 'is_active', 'quantity')
    list_display_links = ('name',)
    list_filter = ['is_active', 'created_at', 'updated_at']
    list_editable = ['price', 'is_active', 'sale_price', 'quantity']
    ordering = ['-created_at']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at',)
    
    # sets up slug to be generated from product
    prepopulated_fields = {'slug' : ('name',)}
    
    
