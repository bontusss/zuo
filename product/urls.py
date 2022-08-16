from django.urls import path

from product.views import product_list, product_detail

app_name = "product"

urlpatterns = [
    path("", product_list, name="index"),
    path("<slug:category_slug>/", product_list, name="product_list_by_category"),
    path("<int:id>/<slug:slug>/", product_detail, name="product_detail"),
]
