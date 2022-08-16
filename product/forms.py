from itertools import product
from django.forms import ModelForm, ValidationError

from product.models import Product


class ProductAdminForm(ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'
        
    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            raise ValidationError('Price must be greater than zero.')
        return self.cleaned_data['price']
