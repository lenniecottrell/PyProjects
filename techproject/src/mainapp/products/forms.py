from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__' #shortcut to say grab all the fields from our product in models