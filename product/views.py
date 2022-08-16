from django.shortcuts import get_object_or_404, render

from category.models import Category
from product.models import Product

# Create your views here.
def product_list(request, category_slug=None):
    categories = Category.objects.filter(is_active=True)
    products = Product.objects.filter(is_active=True)
    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category.slug)
        products = products.filter(category=category)
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'index.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, is_active=True)
    context= {
        'product': product,
    }
    return render(request, '', context)