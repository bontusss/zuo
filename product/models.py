from django.db import models
from django.urls import reverse

from category.models import Category

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(
        max_length=255, unique=True, help_text="Autogenerated from name"
    )
    brand = models.CharField(max_length=50, blank=True)
    sku = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, default=0.00
    )
    sale_duration = models.DurationField('duration')
    sale_time_start = models.DateTimeField(auto_now=False, blank=True, null=True)
    sale_time_end = models.DateTimeField(auto_now=False, blank=True, null=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    is_active = models.BooleanField(default=True)
    quantity = models.IntegerField()
    description = models.TextField()
    more_description = models.TextField(blank=True, null=True)
    meta_keyword = models.CharField(max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField(max_length=255, help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)
    
    class Meta:
        ordering = ['name',]
        index_together = (('id', 'slug'),)
        
    def __str__(self):
        return self.name
    
    # get the duration the sale will last
    def sale_duration(self):
        return self.sale_time_end - self.sale_time_start
        
        
    def get_absolute_url(self):
        return reverse("product:product_detail", args=[self.id, self.slug])
    
    def get_sale_text(self):
        if self.sale_price:
            return 'Sale'
        else:
            return ''
    
    # Get price if product is on sale
    def get_sale_price(self):
        if self.sale_price > self.price:
            return self.price
        else:
            return None